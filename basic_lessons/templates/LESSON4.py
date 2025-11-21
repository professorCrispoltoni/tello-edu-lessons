from djitellopy import Tello

# TODO 1: Create a Tello object and connect to the drone
drone = ...
drone.connect()

drone.takeoff()

# TODO 2: Write the loop for keyboard controls (w, s, a, d, u, j, r, f)
while True:
    c = input("Command: ").lower()

    # TODO: Implement the commands to move the drone
    if c == 'w':
        ...
    elif c == 's':
        ...
    elif c == 'a':
        ...
    elif c == 'd':
        ...
    elif c == 'u':
        ...
    elif c == 'j':
        ...
    elif c == 'r':
        ...
    elif c == 'f':
        ...
    elif c == 'q':
        break

# TODO 3: Land the drone
...
