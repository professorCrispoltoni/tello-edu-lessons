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
        status_label.config(text="✅ Connesso", foreground="green")
        update_status()
    except Exception as e:
        messagebox.showerror("Errore", f"Connessione fallita:\n{e}")
        status_label.config(text="❌ Non connesso", foreground="red")

def check_connection():
    if not connected or tello is None:
        messagebox.showwarning("Drone non connesso", "Prima devi connettere il drone!")
        return False
    return True

def safe_action(func):
    def wrapper():
        if check_connection():
            func()
    return wrapper

@safe_action
def takeoff():
    if tello.get_battery() > 50:
        tello.takeoff()
    else:
        messagebox.showwarning("Batteria bassa", "La batteria è troppo bassa per decollare!")

@safe_action
def land():
    tello.land()

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
@safe_action
def rotate_cw(): tello.rotate_clockwise(30)
@safe_action
def rotate_ccw(): tello.rotate_counter_clockwise(30)

def update_status():
    if connected and tello:
        try:
            battery = tello.get_battery()
            height = tello.get_height()
            temp = tello.get_temperature()
            speed_x, speed_y, speed_z = tello.get_speed_x(), tello.get_speed_y(), tello.get_speed_z()
            battery_var.set(f"{battery}%")
            height_var.set(f"{height} cm")
            temp_var.set(f"{temp} °C")
            speed_var.set(f"{speed_x}, {speed_y}, {speed_z} cm/s")
        except Exception:
            pass
    root.after(3000, update_status)

def on_closing():
    global tello
    if connected and tello:
        try:
            tello.land()
        except:
            pass
    root.destroy()

root = tk.Tk()
root.title("Controllo Drone Tello EDU")
root.geometry("700x400")
root.resizable(False, False)

status_label = ttk.Label(root, text="❌ Non connesso", foreground="red", font=("Segoe UI", 11))
status_label.grid(row=0, column=0, columnspan=2, pady=5)

connect_btn = ttk.Button(root, text="Connetti Drone", command=connect_drone, width=18)
connect_btn.grid(row=1, column=0, columnspan=2, pady=5)

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=2, column=0, sticky="n")

top_frame = ttk.LabelFrame(main_frame, text="Comandi di volo", padding=8)
top_frame.grid(row=0, column=0, pady=5)
ttk.Button(top_frame, text="Decollo", command=takeoff, width=10).grid(row=0, column=0, padx=4, pady=4)
ttk.Button(top_frame, text="Su", command=move_up, width=10).grid(row=0, column=1, padx=4, pady=4)
ttk.Button(top_frame, text="Giù", command=move_down, width=10).grid(row=1, column=1, padx=4, pady=4)
ttk.Button(top_frame, text="Atterra", command=land, width=10).grid(row=1, column=0, padx=4, pady=4)

move_frame = ttk.LabelFrame(main_frame, text="Movimenti direzionali", padding=8)
move_frame.grid(row=1, column=0, pady=5)
ttk.Button(move_frame, text="↑", command=move_forward, width=10).grid(row=0, column=1, pady=3)
ttk.Button(move_frame, text="←", command=move_left, width=10).grid(row=1, column=0, padx=3)
ttk.Button(move_frame, text="→", command=move_right, width=10).grid(row=1, column=2, padx=3)
ttk.Button(move_frame, text="↓", command=move_back, width=10).grid(row=2, column=1, pady=3)

rotate_frame = ttk.LabelFrame(main_frame, text="Rotazioni", padding=8)
rotate_frame.grid(row=2, column=0, pady=5)
ttk.Button(rotate_frame, text="Gira Sinistra", command=rotate_ccw, width=12).grid(row=0, column=0, padx=8, pady=4)
ttk.Button(rotate_frame, text="Gira Destra", command=rotate_cw, width=12).grid(row=0, column=1, padx=8, pady=4)

status_frame = ttk.LabelFrame(root, text="📊 Stato Drone", padding=10)
status_frame.grid(row=2, column=1, padx=10, pady=10, sticky="n")

battery_var = tk.StringVar(value="-")
height_var = tk.StringVar(value="-")
temp_var = tk.StringVar(value="-")
speed_var = tk.StringVar(value="-")

for i, (label, var) in enumerate([("Batteria", battery_var), ("Altezza", height_var),
                                  ("Temperatura", temp_var), ("Velocità (x,y,z)", speed_var)]):
    ttk.Label(status_frame, text=label + ":", font=("Segoe UI", 10, "bold")).grid(row=i, column=0, sticky="w", pady=2)
    ttk.Label(status_frame, textvariable=var, font=("Segoe UI", 10)).grid(row=i, column=1, sticky="w", pady=2)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
