@echo off
REM Creazione della cartella "Drone Tello"
echo Creazione della cartella "Drone Tello"...
mkdir "Drone Tello"
cd "Drone Tello"

REM Creazione dell'ambiente virtuale
echo Creazione dell'ambiente virtuale...
python -m venv venv

REM Impostazione della politica di esecuzione per PowerShell (solo su Windows)
echo Impostazione della politica di esecuzione di PowerShell...
powershell.exe Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

REM Attivazione dell'ambiente virtuale (PowerShell su Windows)
echo Attivazione dell'ambiente virtuale...
call .\venv\Scripts\activate

REM Installazione delle librerie richieste
echo Installazione delle librerie necessarie...
pip install djitellopy==2.5.0
pip install av==14.0.1
pip install opencv-python==4.10.0.84
pip install numpy==1.23.5
pip install pandas==2.2.3
pip install pillow==11.1.0
pip install matplotlib==3.9.4
pip install requests==2.32.3
pip install scipy==1.13.1
pip install seaborn==0.13.2

REM Mostra l'elenco dei pacchetti installati
echo Elenco dei pacchetti installati:
pip list

REM Fine - Mantieni il terminale aperto con l'ambiente attivo
echo L'ambiente virtuale è ora attivo. Puoi eseguire comandi Python.
cmd /k "echo Ambiente attivo. Esegui il tuo codice Python!"
