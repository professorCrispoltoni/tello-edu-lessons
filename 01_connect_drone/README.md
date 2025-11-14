# Lesson 1 – Connecting to the Tello EDU Drone
## 🎯 Objective
Learn how to connect to the Ryze Tello EDU drone using Python and the djitellopy library. Retrieve basic information such as the battery level to verify that communication works correctly.

## 📦 Prerequisites
Before running the script, make sure that:

The drone is powered on and ready to connect (blue LED solid or blinking).

Your computer is connected to the drone's Wi-Fi network (name similar to TELLO-XXXXXX).

Python is installed (version 3.7 or higher recommended).

The djitellopy package is installed. If not, install it with:
```
pip install djitellopy
```

## 📝 Example Code
```
from djitellopy import Tello

tello = Tello()
tello.connect()
print(f"🔋 Battery: {tello.get_battery()}%")
tello.end()
```

This script performs the following actions:

Creates a Tello object.

Connects to the drone.

Reads and prints the battery level.

Closes the connection safely.

## ▶️ How to Run the Script
Turn on the Tello drone.

Connect your computer to the drone's Wi-Fi network.

Open a terminal in the folder where connect_tello.py is located.

Run the command:

```
python connect_tello.py
```
The terminal should display the drone’s battery percentage.

## 🛠️ Common Issues and Solutions
Connection error:
Ensure your computer is connected to the drone’s Wi-Fi and that no other device is connected at the same time.

ImportError for djitellopy:
Check if the library is installed using pip show djitellopy.

## 🔎 Lesson Tips
Try printing other available information, such as temperature, height, or velocity.

Modify the output message format to improve clarity.

## 📚 Useful Links
[djitellopy Documentation](https://djitellopy.readthedocs.io/en/latest/tello/)

## 📝 Student Exercises
- Modify the script to print the drone’s temperature in addition to the battery level.

- Add error handling: display a friendly message if the drone is not connected (try-excpept-finally).

- Research and try to print other telemetry data available through the djitellopy library, such as height or speed.

- Write a short explanation in your own words about why it’s important to call tello.end() at the end of your script.
