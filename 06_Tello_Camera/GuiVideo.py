import threading
import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello
import time

streaming = False
stream_thread = None
tello = Tello()

def update_video():
    frame_read = tello.get_frame_read()
    while streaming:
        frame = frame_read.frame
        frame = cv2.resize(frame, (320, 240))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.config(image=img)
        video_label.image = img
    # Dopo l’uscita dal loop, ferma lo streaming nel drone 
    tello.streamoff()

def connect_drone():
    try:
        tello.connect()
        status_label.config(text="Connesso")
        connect_button.config(state='disabled')
        start_stop_button.config(state='normal')
    except Exception as e:
        messagebox.showerror("Errore di connessione", f"Impossibile connettersi al drone.\n\n{e}")

def start_stream():
    global streaming, stream_thread
    if not streaming:
        try:
            tello.streamon()
        except Exception as e:
            status_label.config(text=f"Errore avvio streaming: {e}")
            return
        streaming = True
        stream_thread = threading.Thread(target=update_video, daemon=True)
        stream_thread.start()
        start_stop_button.config(text="Interrompi streaming")
        root.geometry("300x400")
        video_label.pack()

def stop_stream():
    global streaming, stream_thread
    if streaming:
        streaming = False
        if stream_thread is not None:
            stream_thread.join(timeout=2)  # aspetta massimo 2 sec che il thread termini
        tello.streamoff()
        start_stop_button.config(text="Avvia streaming")
        video_label.config(image='')
        video_label.pack_forget()  # Rimuove il label dalla finestra
        root.geometry("300x200")

def start_stop_stream():
    if streaming:
        stop_stream()
    else:
        start_stream()

root = tk.Tk()
root.title("Controllo Tello Drone")
root.geometry("300x200")
root.resizable(True, True)

status_label = tk.Label(root, text="Non connesso", font=("Arial", 14))
status_label.pack(pady=10)

connect_button = tk.Button(root, text="Connetti drone", command=connect_drone)
connect_button.pack(pady=10)

start_stop_button = tk.Button(root, text="Avvia streaming", command=start_stop_stream, state='disabled')
start_stop_button.pack(pady=10)

video_label = tk.Label(root)
video_label.pack()

root.mainloop()
