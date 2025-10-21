# ⚙️ Setup Ambiente Python per Tello EDU

## 1️⃣ Crea un ambiente virtuale

```bash
python -m venv venv
```

### ▶️ Attiva ambiente

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\env\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

## 2️⃣ Installa librerie richieste

```bash
pip install -r 00_setup_environment/requirements.txt
```

## 3️⃣ Test connessione
Connetti il PC al Wi-Fi del drone (TELLO-XXXXXX) e lancia:

```bash
python 01_connect_drone/connect_tello.py
```
