import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello

# Variabili globali
tello = None
connected = False

def connect_drone():
    global tello, connected
    try:
        tello = Tello()
        tello.connect()
        connected = True
        messagebox.showinfo("Connessione", "Drone connesso con successo!")
        status_label.config(text="Connesso", foreground="green")
        update_drone_status()
    except Exception as e:
        messagebox.showerror("Errore di connessione", f"Impossibile connettersi al drone.\n\n{e}")
        status_label.config(text="Non connesso", foreground="red")

def update_drone_status():
    if connected and tello:
        try:
            battery = tello.get_battery()
            temp = tello.get_temperature()
            height = tello.get_height()

            battery_var.set(f"{battery}%")
            temp_var.set(f"{temp}°C")
            height_var.set(f"{height} cm")

            status_label.config(text=f"Connesso • Batteria {battery}%", foreground="green")
        except Exception:
            status_label.config(text="Errore lettura dati", foreground="orange")

    root.after(3000, update_drone_status)

# Costruzione GUI
root = tk.Tk()
root.title("Drone Tello GUI")
root.geometry("320x250")
root.resizable(False, False)

# Variabili Tkinter per dati drone
battery_var = tk.StringVar(value="")
temp_var = tk.StringVar(value="")
height_var = tk.StringVar(value="")

status_label = ttk.Label(root, text="Non connesso", foreground="red", font=("Segoe UI", 11))
status_label.pack(pady=10)

connect_btn = ttk.Button(root, text="Connetti Drone", command=connect_drone, width=20)
connect_btn.pack(pady=10)

# Frame dedicato ai dati del drone
data_frame = ttk.LabelFrame(root, text="Dati Drone", padding=10)
data_frame.pack(padx=20, pady=10, fill="x")

ttk.Label(data_frame, text="Batteria:", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w")
ttk.Label(data_frame, textvariable=battery_var, font=("Segoe UI", 10)).grid(row=0, column=1, sticky="e", padx=10)

ttk.Label(data_frame, text="Temperatura:", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w")
ttk.Label(data_frame, textvariable=temp_var, font=("Segoe UI", 10)).grid(row=1, column=1, sticky="e", padx=10)

ttk.Label(data_frame, text="Altezza:", font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w")
ttk.Label(data_frame, textvariable=height_var, font=("Segoe UI", 10)).grid(row=2, column=1, sticky="e", padx=10)

root.mainloop()
