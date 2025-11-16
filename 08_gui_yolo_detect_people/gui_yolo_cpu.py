import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello
import cv2
from PIL import Image, ImageTk
import threading
import time
import torch
from ultralytics import YOLO

# Carica modello YOLO appena avviato
model = YOLO('yolov8n.pt')  # Modello nano per CPU
device = 'cpu'
model.to(device)

# ==========================
# Variabili globali
# ==========================
tello = None
connected = False
streaming = False
frame_buffer = None
frame_counter = 0
last_processed_frame = None  # per mantenere visibilità

# ==========================
# Funzioni di controllo
# ==========================
def connect_drone():
    global tello, connected
    try:
        tello = Tello()
        tello.connect()
        connected = True
        messagebox.showinfo("Connessione", "Drone connesso con successo!")
        status_label.config(text="✅ Connesso", foreground="green")
        signal_label.config(text="🟢 Operativo", foreground="green")
        update_drone_status()
    except Exception as e:
        messagebox.showerror("Errore di connessione", f"Impossibile connettersi al drone.\n\n{e}")
        status_label.config(text="❌ Non connesso", foreground="red")
        signal_label.config(text="🔴 Non operativo", foreground="red")

def reconnect_drone():
    global tello, connected
    stop_video_stream()
    try:
        tello.end()
    except:
        pass
    connected = False
    signal_label.config(text="🟡 Tentativo di riconnessione...", foreground="orange")
    root.after(500, connect_drone)

def check_connection():
    if not connected or tello is None:
        messagebox.showwarning("Drone non connesso", "Prima devi connettere il drone!")
        return False
    return True

def safe_action(func):
    def wrapper():
        if check_connection():
            try:
                func()
                signal_label.config(text="🟢 Operativo", foreground="green")
            except Exception as e:
                signal_label.config(text="🔴 Errore comando", foreground="red")
                messagebox.showerror("Errore", str(e))
    return wrapper

@safe_action
def takeoff():
    if tello.get_battery() > 35:
        tello.takeoff()
    else:
        messagebox.showwarning("Batteria bassa", "La batteria è troppo bassa per decollare!")

@safe_action
def land():
    tello.land()

@safe_action
def move_forward():
    tello.move_forward(30)

@safe_action
def move_back():
    tello.move_back(30)

@safe_action
def move_left():
    tello.move_left(30)

@safe_action
def move_right():
    tello.move_right(30)

@safe_action
def move_up():
    tello.move_up(30)

@safe_action
def move_down():
    tello.move_down(30)

@safe_action
def rotate_cw():
    tello.rotate_clockwise(30)

@safe_action
def rotate_ccw():
    tello.rotate_counter_clockwise(30)

# ==========================
# Streaming e rilevamento persone
# ==========================
def start_video_stream():
    global streaming, frame_thread
    if not check_connection():
        return
    if not streaming:
        try:
            tello.streamon()
            streaming = True
            frame_thread = threading.Thread(target=frame_capture_loop, daemon=True)
            frame_thread.start()
            root.after(0, update_video_gui)
            messagebox.showinfo("Video", "Streaming video avviato.")
            signal_label.config(text="🟢 Video attivo", foreground="green")
        except Exception as e:
            messagebox.showerror("Errore video", f"Impossibile avviare lo streaming.\n\n{e}")
            signal_label.config(text="🔴 Errore video", foreground="red")

def frame_capture_loop():
    global frame_buffer, frame_counter, last_processed_frame
    frame_read = tello.get_frame_read()
    while streaming:
        frame_buffer = frame_read.frame
        frame_counter += 1
        time.sleep(0.01)

def detect_people_in_frame(frame):
    results = model(frame)
    count = 0
    for result in results[0].boxes:
        cls_id = int(result.cls[0].item())
        if cls_id == 0:  # Persona
            count += 1
            box = result.xyxy[0].tolist()
            x1, y1, x2, y2 = map(int, box)
            confidence = result.conf[0].item()
            # Disegna bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f'Person {confidence:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    return frame, count

def update_video_gui():
    global frame_buffer, frame_counter, last_processed_frame
    if frame_buffer is not None:
        frame = frame_buffer.copy()
        frame = cv2.resize(frame, (320, 240))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Esegui rilevamento ogni 3 frame
        if frame_counter % 3 == 0:
            frame, person_count = detect_people_in_frame(frame)
            people_count_var.set(str(person_count))
            last_processed_frame = frame
        else:
            # Mostra l’ultimo frame elaborato
            frame = getattr(update_video_gui, 'last_frame', frame)
        # Aggiorna immagine
        img_tk = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.imgtk = img_tk
        video_label.configure(image=img_tk)

    if streaming:
        root.after(33, update_video_gui)

def stop_video_stream():
    global streaming
    streaming = False
    try:
        tello.streamoff()
    except:
        pass

# ==========================
# Stato drone e GUI
# ==========================
def update_drone_status():
    if connected and tello:
        try:
            battery = tello.get_battery()
            height = tello.get_height()
            temp = tello.get_temperature()
            battery_var.set(f"{battery}%")
            height_var.set(f"{height} cm")
            temp_var.set(f"{temp}°C")
            status_label.config(text=f"✅ Connesso • Batteria {battery}%", foreground="green")
        except:
            status_label.config(text="⚠️ Errore lettura dati", foreground="orange")
            signal_label.config(text="🔴 Errore comunicazione", foreground="red")
    root.after(3000, update_drone_status)

# ==========================
# Chiusura e cleanup
# ==========================
def on_closing():
    global tello
    stop_video_stream()
    if connected and tello:
        try:
            tello.land()
        except:
            pass
    root.destroy()

# ==========================
# Costruzione GUI
# ==========================
root = tk.Tk()
root.title("Controllo Drone Tello")
root.geometry("800x600")
root.resizable(False, False)

# Variabile per conteggio persone
people_count_var = tk.StringVar(value="0")

# Style GUI
style = ttk.Style(root)
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
style.map("TButton", background=[("active", "#007acc")], foreground=[("active", "white")])

# Layout principale
main_container = ttk.Frame(root, padding=10)
main_container.pack(fill="both", expand=True)
main_container.columnconfigure(0, weight=1)
main_container.columnconfigure(1, weight=0)

# Colonna sinistra
left_frame = ttk.Frame(main_container)
left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
status_label = ttk.Label(left_frame, text="❌ Non connesso", foreground="red", font=("Segoe UI", 11))
status_label.pack(pady=5)
connect_btn = ttk.Button(left_frame, text="Connetti Drone", command=connect_drone, width=18)
connect_btn.pack(pady=5)

control_frame = ttk.Frame(left_frame, padding=10)
control_frame.pack()

# Comandi volo
top_frame = ttk.LabelFrame(control_frame, text="Comandi di volo", padding=8)
top_frame.grid(row=0, column=0, pady=5)
ttk.Button(top_frame, text="Decollo", command=takeoff, width=10).grid(row=0, column=0, padx=4, pady=4)
ttk.Button(top_frame, text="Su", command=move_up, width=10).grid(row=0, column=1, padx=4, pady=4)
ttk.Button(top_frame, text="Giù", command=move_down, width=10).grid(row=1, column=1, padx=4, pady=4)
ttk.Button(top_frame, text="Atterra", command=land, width=10).grid(row=1, column=0, padx=4, pady=4)

move_frame = ttk.LabelFrame(control_frame, text="Movimenti direzionali", padding=8)
move_frame.grid(row=1, column=0, pady=5)
ttk.Button(move_frame, text="↑", command=move_forward, width=10).grid(row=0, column=1, pady=3)
ttk.Button(move_frame, text="←", command=move_left, width=10).grid(row=1, column=0, padx=3)
ttk.Button(move_frame, text="→", command=move_right, width=10).grid(row=1, column=2, padx=3)
ttk.Button(move_frame, text="↓", command=move_back, width=10).grid(row=2, column=1, pady=3)

rotate_frame = ttk.LabelFrame(control_frame, text="Rotazioni", padding=8)
rotate_frame.grid(row=2, column=0, pady=5)
ttk.Button(rotate_frame, text="Gira Sinistra", command=rotate_ccw, width=12).grid(row=0, column=0, padx=6, pady=4)
ttk.Button(rotate_frame, text="Gira Destra", command=rotate_cw, width=12).grid(row=0, column=1, padx=6, pady=4)

# Colonna destra
right_frame = ttk.LabelFrame(main_container, text="Stato Drone", padding=10)
right_frame.grid(row=0, column=1, sticky="n", padx=(5, 0))
battery_var = tk.StringVar(value="N/D")
height_var = tk.StringVar(value="N/D")
temp_var = tk.StringVar(value="N/D")
ttk.Label(right_frame, text="Batteria:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
ttk.Label(right_frame, textvariable=battery_var, font=("Segoe UI", 10)).pack(anchor="w", pady=3)
ttk.Label(right_frame, text="Altezza:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
ttk.Label(right_frame, textvariable=height_var, font=("Segoe UI", 10)).pack(anchor="w", pady=3)
ttk.Label(right_frame, text="Temperatura:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
ttk.Label(right_frame, textvariable=temp_var, font=("Segoe UI", 10)).pack(anchor="w", pady=3)

# Nuovo: contatore persone rilevate
ttk.Label(right_frame, text="Persone rilevate:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=3)
ttk.Label(right_frame, textvariable=people_count_var, font=("Segoe UI", 10), foreground="blue").pack(anchor="w", pady=3)

signal_label = ttk.Label(right_frame, text="🔴 Non operativo", foreground="red", font=("Segoe UI", 10, "bold"))
signal_label.pack(anchor="center", pady=8)

# Video
video_frame = ttk.LabelFrame(right_frame, text="Video", padding=5)
video_frame.pack(pady=10)
video_label = ttk.Label(video_frame)
video_label.pack()
ttk.Button(video_frame, text="Avvia Video", command=start_video_stream).pack(pady=5)

# Main loop
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
