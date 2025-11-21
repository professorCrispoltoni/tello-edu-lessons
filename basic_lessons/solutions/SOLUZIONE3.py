from djitellopy import Tello

# Create a Tello object and connect to the drone
drone = Tello()
drone.connect()

# Create a log file
log = open("flight_log.txt", "w")

# Write a function to log the state (battery, height)
def log_state():
    battery = drone.get_battery()
    height = drone.get_height()
    log.write(f"STATE -> Battery: {battery}%, Height: {height} cm\n")
    log.flush()

# Write a function to log movements
def log_move(action, value):
    log.write(f"MOVEMENT -> {action} {value}\n")
    log.flush()

# Perform some movements and log them
drone.takeoff()
log_state()

drone.move_forward(50)
log_move("forward", 50)
log_state()

drone.move_up(30)
log_move("up", 30)
log_state()

drone.move_right(40)
log_move("right", 40)
log_state()

# Close the log file at the end
drone.land()
log_state()
log.close()
