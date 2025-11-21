from djitellopy import Tello
import time

# Create a Tello object and connect to the drone
drone = Tello()
drone.connect()

# Write a function that draws a square
def draw_square(drone, side):
    for _ in range(4):
        drone.move_forward(side)
        time.sleep(1)
        drone.rotate_clockwise(90)
        time.sleep(1)

# Make the drone take off
drone.takeoff()

# Make the drone draw a square
draw_square(drone, 50)

# Make the drone land
drone.land()
