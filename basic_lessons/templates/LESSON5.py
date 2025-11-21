from djitellopy import Tello
import cv2
import time
import os

# TODO 1: Create a Tello object and connect to the drone
drone = ...
drone.connect()

# TODO 2: Start video streaming
drone.streamon()
frame_read = drone.get_frame_read()

# TODO 3: Create a folder to save the photos
folder = "fotos"
os.makedirs(folder, exist_ok=True)

# TODO 4: take N photos during rotations
num_photos = ...

drone.takeoff()

for i in range(...):
    frame = frame_read.frame

    # TODO: Save the photos
    filename = f"{folder}/photo_{i}.jpg"
    cv2.imwrite(filename, frame)

    # TODO: Rotate the drone by the calculated angle
    ...

# TODO 5: Land the drone
drone.land()
