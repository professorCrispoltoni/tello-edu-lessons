import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello

drone = None
connected = False
flying = False

def connect_drone():
    global drone, connected
    try:
        drone = Tello()
        drone.connect()
        connected = True
        messagebox.showinfo("Connessione", "Drone connesso con successo!")
        status_label.config(text="Connesso", foreground="green")
    except Exception as e:
        messagebox.showerror("Errore di connessione", f"Impossibile connettersi al drone.\n\n{e}")
        status_label.config(text="Non connesso", foreground="red")

def takeoff():    
    if drone.get_battery() > 35:
        drone.takeoff()
        flying = True
    else:
        messagebox.showwarning("Batteria low", "Battery too low to take off!")
        
def land(): 
    if connected and flying:
        drone.land()
        
def on_closing():
    if connected and drone:
        try:
            drone.land()
        except:
            pass
    window.destroy()

# CREATE GUI
window = tk.Tk()

window.title("Drone Controller")
window.geometry("300x200")
window.resizable(False, False)

status_label = tk.Label(window, text="Non connesso", foreground="red", font=("Segoe UI", 11))
status_label.pack(pady=5)

connect_btn = tk.Button(window, text="Connect", command=connect_drone)
connect_btn.pack(pady=10)

takeOff_btn = tk.Button(window, text="Takeoff", command=takeoff)
takeOff_btn.pack(pady=10)

land_btn = tk.Button(window, text="Land", command=land)
land_btn.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
