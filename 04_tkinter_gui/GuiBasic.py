import tkinter as tk
from tkinter import ttk, messagebox
from djitellopy import Tello

# ===========================
# VARIABILI GLOBALI
# ===========================
tello = None         # Oggetto drone (istanza Tello)
connected = False    # Stato connessione drone (False = non connesso)

# ===========================
# FUNZIONE DI CONNESSIONE
# ===========================
def connect_drone():
    """
    Tenta la connessione al drone Tello.
    - Crea un'istanza Tello.
    - Connette il drone.
    - Modifica lo stato globale connected.
    - Aggiorna la GUI con notifiche e stato.
    - Avvia l'aggiornamento periodico del livello batteria.
    """
    global tello, connected
    try:
        tello = Tello()         # Crea istanza drone
        tello.connect()         # Connette il drone
        connected = True        # Aggiorna stato a connesso
        messagebox.showinfo("Connessione", "Drone connesso con successo!")
        status_label.config(text="Connesso", foreground="green")
        update_drone_status()   # Avvia aggiornamento del livello batteria
    except Exception as e:
        # Gestione errori connessione
        messagebox.showerror("Errore di connessione", f"Impossibile connettersi al drone.\n\n{e}")
        status_label.config(text="Non connesso", foreground="red")

# ===========================
# FUNZIONE AGGIORNAMENTO BATTERIA
# ===========================
def update_drone_status():
    """
    Aggiorna periodicamente (ogni 3 secondi) il livello di batteria del drone nella GUI.
    Se il drone è connesso tenta di leggere il livello batteria.
    Alla riuscita aggiorna label con percentuale batteria.
    In caso di errore aggiorna la label con un messaggio di errore.
    """
    if connected and tello:
        try:
            battery = tello.get_battery()   # Lettura livello batteria (%)
            battery_var.set(f"{battery}%")  # Aggiorna variabile associata all'etichetta GUI
            status_label.config(text=f"Connesso • Batteria {battery}%", foreground="green")
        except Exception:
            status_label.config(text="Errore lettura dati", foreground="orange")

    # Richiama se stessa dopo 3000ms (3 secondi) per aggiornamento continuo
    root.after(3000, update_drone_status)

# ===========================
# COSTRUZIONE DELLA GUI
# ===========================
root = tk.Tk()
root.title("Drone Tello GUI")
root.geometry("300x150")    # Dimensioni fisse della finestra
root.resizable(False, False)  # Disabilita ridimensionamento

# Variabile Tkinter per mostrare il livello di batteria dinamicamente
battery_var = tk.StringVar(value="")

# Label per mostrare lo stato di connessione (testo e colore)
status_label = ttk.Label(root, text="Non connesso", foreground="red", font=("Segoe UI", 11))
status_label.pack(pady=10)

# Bottone per connettere il drone che chiama la funzione connect_drone al click
connect_btn = ttk.Button(root, text="Connetti Drone", command=connect_drone, width=20)
connect_btn.pack(pady=10)

# Label per mostrare in tempo reale la percentuale di batteria
battery_label = ttk.Label(root, textvariable=battery_var, font=("Segoe UI", 12))
battery_label.pack(pady=5)

# Avvia il loop principale della GUI (attesa eventi, aggiornamenti...)
root.mainloop()
