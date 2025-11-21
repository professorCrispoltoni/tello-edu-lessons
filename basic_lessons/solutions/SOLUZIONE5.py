from djitellopy import Tello
import cv2
import time
import os

# Create a Tello object and connect to the drone
drone = Tello()
drone.connect()

# Start video streaming
drone.streamon()
frame_read = drone.get_frame_read()

# Create a folder to save the photos
folder = "fotos"
os.makedirs(folder, exist_ok=True)

# Ask the user how many photos to take
num_photos = int(input("How many photos to take? "))

# Calculate the rotation angle
angle = 360 / num_photos

drone.takeoff()

# Take photos during rotations
for i in range(num_photos):
    frame = frame_read.frame

    # Save the photo
    filename = f"{folder}/photo_{i}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved {filename}")

    # Rotate the drone by the calculated angle
    drone.rotate_clockwise(int(angle))

# Land the drone
drone.land()
