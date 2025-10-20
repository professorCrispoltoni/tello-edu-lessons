import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello

tello = None
connected = False

def connect_drone():
    global tello, connected
    try:
        tello = Tello()
        tello.connect()
        connected = True
        battery = tello.get_battery()
        messagebox.showinfo("Connesso", f"Batteria: {battery}%")
    except Exception as e:
        messagebox.showerror("Errore", f"Connessione fallita:\n{e}")

def safe_action(func):
    def wrapper():
        if connected:
            func()
        else:
            messagebox.showwarning("Attenzione", "Connetti prima il drone!")
    return wrapper

@safe_action
def takeoff(): tello.takeoff()

@safe_action
def land(): tello.land()

@safe_action
def move_forward(): tello.move_forward(30)
@safe_action
def move_back(): tello.move_back(30)
@safe_action
def move_left(): tello.move_left(30)
@safe_action
def move_right(): tello.move_right(30)
@safe_action
def move_up(): tello.move_up(30)
@safe_action
def move_down(): tello.move_down(30)

root = tk.Tk()
root.title("Tello EDU GUI")
root.geometry("400x400")

ttk.Button(root, text="Connetti Drone", command=connect_drone).pack(pady=10)
ttk.Button(root, text="Decollo", command=takeoff).pack(pady=5)
ttk.Button(root, text="Atterra", command=land).pack(pady=5)

root.mainloop()
