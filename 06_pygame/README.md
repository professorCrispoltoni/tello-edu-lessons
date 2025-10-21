# 🛸 DJI Tello Keyboard Controller (con Pygame)

Questo progetto permette di **pilotare un drone DJI Tello** dal computer utilizzando la **tastiera** e visualizzando in tempo reale il **flusso video** della telecamera del drone.

Il controllo e la visualizzazione sono gestiti tramite **Pygame** e **OpenCV**.

---

## 🎯 Funzionalità

✅ Controllo completo del drone con la tastiera  
✅ Visualizzazione video in tempo reale  
✅ Indicatore di livello della batteria  
✅ Frequenza di aggiornamento stabile (FPS)  
✅ Chiusura sicura e rilascio delle risorse

---

## 🎮 Comandi da tastiera

| Tasto | Azione |
|-------|--------|
| **T** | Decollo |
| **L** | Atterraggio |
| **↑** | Avanti |
| **↓** | Indietro |
| **←** | Sinistra |
| **→** | Destra |
| **W** | Salita |
| **S** | Discesa |
| **A** | Rotazione antioraria |
| **D** | Rotazione oraria |
| **ESC** | Esci dal programma |

---

## ⚙️ Dipendenze

Assicurati di avere installato:

```bash
pip install djitellopy opencv-python pygame numpy
🚀 Avvio del programma
Accendi il drone DJI Tello.
```

Connettiti alla rete Wi-Fi del drone (TELLO-XXXXXX).

Esegui il programma Python:

```
python tello_controller.py
```

Si aprirà una finestra con il video del drone.

Usa la tastiera per controllare il volo!

🧩 Struttura del progetto
- FrontEnd: classe principale che gestisce video, input e comandi.

- run(): ciclo principale del programma (loop video e comandi).

- keydown() / keyup(): rilevano i tasti premuti e aggiornano la velocità del drone.

- update(): invia i comandi di movimento al drone a intervalli regolari.

🧠 Perché usare Pygame?
L’uso di Pygame è una scelta strategica per rendere il controllo più fluido e semplice:

Motivo	Descrizione
- Gestione input precisa	Pygame rileva i tasti premuti e rilasciati in modo affidabile e continuo.
- Visualizzazione video	Permette di mostrare il flusso video del drone in una finestra interattiva.
- Timer stabile (FPS)	Garantisce aggiornamenti regolari dei comandi (es. 120 volte al secondo).
- Integrazione GUI	Tutto (video + input + testo) in una sola finestra, senza librerie aggiuntive.
- Portabilità	Funziona su Windows, macOS e Linux senza configurazioni complesse.

🧰 Esempio di uscita video
Durante il volo, nella finestra Pygame viene mostrato:

- Il flusso video del drone.

- Il livello della batteria in basso a sinistra.

- L’immagine ruotata correttamente per la visualizzazione.

🪄 Suggerimenti
Evita di chiudere il programma forzatamente: usa ESC per uscire in sicurezza.

Se non vedi il video, prova a eseguire prima:

```
tello.streamoff()
tello.streamon()
```

Puoi modificare la velocità del drone cambiando il valore della costante S.
