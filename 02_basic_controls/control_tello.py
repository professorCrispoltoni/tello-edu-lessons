from djitellopy import Tello
import time

tello = Tello()
tello.connect()

if tello.get_battery() > 20:
    tello.takeoff()
    tello.move_up(50)
    tello.rotate_clockwise(90)
    tello.move_forward(100)
    tello.land()
else:
    print("⚠️ Batteria troppo bassa per volare")

tello.end()
