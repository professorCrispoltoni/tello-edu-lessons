import tkinter as tk
from tkinter import messagebox
from djitellopy import Tello

# Global variables
tello = None
connected = False
flying = False  # Global variable to track if the drone is flying

def connect_drone():
    global tello, connected
    try:
        tello = Tello()
        tello.connect()
        connected = True
        status_label.config(text="Connected", foreground="green")
        messagebox.showinfo("Connection", "Drone connected successfully!")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to the drone.\n\n{e}")
        status_label.config(text="Not connected", foreground="red")

def takeoff():
    global flying  # Declare flying as global
    if connected and tello:
        tello.takeoff()
        status_label.config(text="Flying", foreground="blue")
        flying = True  # Update the flying status
    else:
        messagebox.showwarning("Error", "You must connect the drone first!")

def land():
    global flying  # Declare flying as global
    if connected and flying:
        tello.land()
        status_label.config(text="Landed", foreground="red")
        flying = False  # Update the flying status
    else:
        messagebox.showwarning("Error", "Drone is not flying!")

# Create the main window
root = tk.Tk()
root.title("Drone Control GUI")
root.geometry("300x250")
root.resizable(False, False)

# Status label to display connection status
status_label = tk.Label(root, text="Not connected", foreground="red", font=("Segoe UI", 12))
status_label.pack(pady=20)

# Connect button
connect_btn = tk.Button(root, text="Connect", command=connect_drone)
connect_btn.pack(pady=5)

# Takeoff button
takeoff_btn = tk.Button(root, text="Takeoff", command=takeoff)
takeoff_btn.pack(pady=5)

# Land button
land_btn = tk.Button(root, text="Land", command=land)
land_btn.pack(pady=5)

# Start the main event loop
root.mainloop()
