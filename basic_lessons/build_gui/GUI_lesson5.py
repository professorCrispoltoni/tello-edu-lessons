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
        update_drone_status()  # Start periodic update
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to the drone.\n\n{e}")
        status_label.config(text="Not connected", foreground="red")

def update_drone_status():
    if connected and tello:
        try:
            battery = tello.get_battery()  # Get battery percentage
            battery_var.set(f"Battery: {battery}%")  # Update battery label
            altitude = tello.get_height()  # Get altitude (height)
            altitude_var.set(f"Altitude: {altitude}m")  # Update altitude label
        except Exception:
            status_label.config(text="Error reading data", foreground="orange")
    
    # Update every 3000ms (3 seconds)
    root.after(3000, update_drone_status)

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
root.geometry("350x450")  # Adjusted for two frames
root.resizable(False, False)

# Frame for sensor data (battery, altitude) with a border and background
sensor_frame = tk.Frame(root, relief="solid", bd=2, padx=10, pady=10)
sensor_frame.pack(pady=20, padx=10, fill="both", expand=True)

# Frame for control buttons (connect, takeoff, land) with a border and background
button_frame = tk.Frame(root, relief="solid", bd=2, padx=10, pady=10)
button_frame.pack(pady=20, padx=10, fill="both", expand=True)

# Status label to display connection status
status_label = tk.Label(sensor_frame, text="Not connected", foreground="red", font=("Segoe UI", 12))
status_label.pack(pady=10)

# Battery and altitude labels
battery_var = tk.StringVar(value="Battery: 0%")
altitude_var = tk.StringVar(value="Altitude: 0m")

battery_label = tk.Label(sensor_frame, textvariable=battery_var, font=("Segoe UI", 12))
battery_label.pack(pady=5)

altitude_label = tk.Label(sensor_frame, textvariable=altitude_var, font=("Segoe UI", 12))
altitude_label.pack(pady=5)

# Control buttons (Connect, Takeoff, Land)
connect_btn = tk.Button(button_frame, text="Connect", command=connect_drone)
connect_btn.pack(pady=5)

takeoff_btn = tk.Button(button_frame, text="Takeoff", command=takeoff)
takeoff_btn.pack(pady=5)

land_btn = tk.Button(button_frame, text="Land", command=land)
land_btn.pack(pady=5)

# Start the main event loop
root.mainloop()
