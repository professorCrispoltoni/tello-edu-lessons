# ⚙️ Setup Ambiente Python per Tello EDU

## 1️⃣ Crea un ambiente virtuale

```bash
python -m venv venv

▶️ Attiva ambiente
Windows (PowerShell):

powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\activate

2️⃣ Installa librerie richieste
pip install -r 00_setup_environment/requirements.txt

3️⃣ Test connessione
Connetti il PC al Wi-Fi del drone (TELLO-XXXXXX) e lancia:

python 01_connect_drone/connect_tello.py

### 📄 `00_setup_environment/requirements.txt`

```txt
djitellopy>=2.5.0
opencv-python
numpy
keyboard
