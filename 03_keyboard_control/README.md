# Lesson 3 – Real-Time Drone Control with Keyboard

## 🎯 Objective
Control the Ryze Tello EDU drone in real time using keyboard commands to move, rotate, ascend, descend, and land safely.

## 📦 Prerequisites
Make sure your PC is connected to the Tello’s Wi-Fi.
Python 3.7+ with the djitellopy installed (pip install djitellopy).
Drone battery level should be above 20% for safety.

## Key Controls
w - move forward 30 cm

s - move backward 30 cm

a - move left 30 cm

d - move right 30 cm

e - rotate clockwise 30°

q - rotate counterclockwise 30°

r - move up 30 cm

f - move down 30 cm

l - land immediately

ESC - exit control loop

## ▶️ How to Run
Turn on the Tello drone and connect your computer to its Wi-Fi.

Save the script as control_tello_realtime.py.

Run the script from your terminal:

```
python control_tello_realtime.py
```

Use the keyboard keys above to fly the drone in real time.

## ⚠️ Safety Notes
Always keep the drone within line of sight.

Use safe indoor or open outdoor spaces.

Land the drone (l key) before exiting to avoid crashes.
