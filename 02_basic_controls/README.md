# Lesson 2 – Basic Flight Commands

## 🎯 Objective
Execute fundamental commands: takeoff, movements, and landing.

## ▶️ Execution
```
python control_tello.py
```

Basic flight commands for the Tello drone in English are as follows:

- takeoff(): This command makes the drone take off and hover at a low altitude automatically.

- land(): This safely lands the drone on the ground.

- move_up(distance_cm): Moves the drone straight up by the specified distance in centimeters.

- move_down(distance_cm): Moves the drone straight down by the specified distance in centimeters.

- move_forward(distance_cm): Moves the drone forward by the given distance in centimeters.

- move_back(distance_cm): Moves the drone backward by the specified distance.

- move_left(distance_cm) and move_right(distance_cm): Move the drone left or right respectively by the given distance.

- rotate_clockwise(degrees): Rotates the drone clockwise by the specified angle in degrees (e.g., 90).

- rotate_counter_clockwise(degrees): Rotates the drone counterclockwise by the specified degrees.

These commands give basic control of the drone’s position and orientation in 3D space. They are typically executed in sequence to perform flight maneuvers. The drone automatically stabilizes itself after each move or rotation command. Flight can only be initiated if the battery level is sufficient and the drone is properly connected.

This set of commands is accessible through the djitellopy Python library, allowing script-based drone control for educational and development purposes.
