# 🛸 Tello EDU Python Lessons

Percorso passo–passo per imparare a controllare il drone **Ryze Tello EDU** con **Python**.

Dalla connessione di base fino alla creazione di una **GUI interattiva con Tkinter**.

---

## 📚 Lezioni

| Lezione | Descrizione |
|----------|-------------|
| [00_setup_environment](00_setup_environment) | Setup ambiente virtuale e librerie |
| [01_connect_drone](01_connect_drone) | Connessione e test batteria |
| [02_basic_controls](02_basic_controls) | Comandi base di volo |
| [03_keyboard_control](03_keyboard_control) | Controllo via tastiera |
| [04_tkinter_gui](04_tkinter_gui) | GUI base con pulsanti Tkinter |
| [05_tkinter_gui_status](05_tkinter_gui_status) | GUI avanzata con feedback di stato |

---

## ⚙️ Requisiti
- Python 3.8+
- Drone **Ryze Tello EDU**
- PC connesso al Wi-Fi del drone

---

## 🚀 Avvio rapido

```bash
git clone https://github.com/<tuo-utente>/tello-edu-lessons.git
cd tello-edu-lessons
python -m venv venv
.\venv\Scripts\activate     # su Windows
pip install -r 00_setup_environment/requirements.txt
python 01_connect_drone/connect_tello.py
