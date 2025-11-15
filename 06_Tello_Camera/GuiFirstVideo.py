import threading
import cv2
from PIL import Image, ImageTk
import tkinter as tk
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

root = tk.Tk()
video_label = tk.Label(root)
video_label.pack()

def update_video():
    frame_read = tello.get_frame_read()
    while True:
        frame = frame_read.frame
        frame = cv2.resize(frame, (320, 240))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # COLOR_BGR2GRAY
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.config(image=img)
        video_label.image = img

threading.Thread(target=update_video, daemon=True).start()
root.mainloop()
