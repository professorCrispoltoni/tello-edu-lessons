from djitellopy import Tello

# Create a Tello object and connect to the drone
drone = Tello()
drone.connect()

drone.takeoff()

# Write the loop for keyboard controls (w, s, a, d, u, j, r, f)
while True:
    c = input("Command: ").lower()

    if c == 'w':
        drone.move_forward(30)
    elif c == 's':
        drone.move_back(30)
    elif c == 'a':
        drone.move_left(30)
    elif c == 'd':
        drone.move_right(30)
    elif c == 'u':
        drone.move_up(30)
    elif c == 'j':
        drone.move_down(30)
    elif c == 'r':
        drone.rotate_clockwise(45)
    elif c == 'f':
        drone.rotate_counter_clockwise(45)
    elif c == 'q':
        break

# Land the drone
drone.land()
