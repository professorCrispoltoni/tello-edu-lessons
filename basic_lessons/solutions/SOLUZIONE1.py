from djitellopy import Tello

# Create a Tello object
drone = Tello()

# Connect to the drone
drone.connect()

# Print battery level and current altitude
battery = drone.get_battery()
height = drone.get_height()
print(f"Battery: {battery}%")
print(f"Height: {height} cm")

# Make the drone take off
drone.takeoff()

# Move the drone up by 30 cm
drone.move_up(30)

# Rotate the drone by 90 degrees clockwise
drone.rotate_clockwise(90)

# Move the drone down by 30 cm
drone.move_down(30)

# Land the drone
drone.land()
