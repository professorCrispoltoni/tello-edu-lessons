from djitellopy import Tello

# TODO 1: Create a Tello object and connect to the drone
drone = ...
drone.connect()

# TODO 2: Create a log file
log = ...

# TODO 3: Write a function to log the state (battery, height)
def log_state():
    battery = ...
    height = ...
    log.write(f"STATE -> Battery: {battery}%, Height: {height} cm\n")
    log.flush()

# TODO 4: Write a function to log movements
def log_move(action, value):
    log.write(f"MOVEMENT -> {action} {value}\n")
    log.flush()

# TODO 5: Perform some movements and log them
...

# TODO 6: Close the log file
...
