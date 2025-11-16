# Tello Drone Control with Live Video Streaming and Person Detection using YOLOv8

## Project Description

This project enables controlling a Tello drone with a Tkinter graphical interface, displaying the live video stream from the drone's camera. It integrates a person detection system based on the YOLOv8 model, which analyzes each video frame to locate and count people in the scene.

The application runs efficiently even on PCs without NVIDIA GPUs or CUDA support by performing detection on the CPU and optimizing performance by running inference every 3 frames.

---

## How Person Detection with YOLOv8 Works

YOLOv8 (You Only Look Once, version 8) is a deep learning model designed for real-time object detection. Unlike approaches that scan the image multiple times, YOLO processes the entire image in a single pass by dividing it into a grid and predicting bounding boxes and classes simultaneously for each grid cell. This makes it extremely fast and efficient.

In this project:
- Each video frame from the drone is resized and passed to the YOLOv8 model.
- The model outputs detected objects, each with bounding box coordinates, class label (e.g., "person"), and confidence score.
- The code filters detected objects to only those classified as "person" (class ID 0).
- For each detected person, a green bounding box with confidence is drawn on the video frame.
- The total number of people detected is counted and updated in real-time on the GUI.
- To ensure smooth video playback and reduce CPU load, detection runs every 3 frames instead of every frame.

This integration provides an interactive drone control experience enhanced by AI-powered visual analysis, useful for educational purposes, surveillance, or robotics research.

---

## Usage Instructions

- Make sure to install dependencies: `djitellopy`, `ultralytics`, `torch`, `opencv-python`, `Pillow`, and `tkinter`.
- Run the main Python script.
- Click "Connect Drone" to establish a connection with the drone.
- Click "Start Video" to begin video streaming and person detection.
- View the video feed with green boxes around detected people and see the live count updated in the "People Detected" section.

---

## Limitations and Notes

- The YOLOv8 nano model used is lightweight and designed for CPU usage, but inference is slower without a GPU.
- Running detection every N frames helps balance speed and accuracy.
- On systems with compatible NVIDIA GPUs, enabling CUDA can greatly improve performance.

---

## References

- [YOLOv8 - Ultralytics Official](https://ultralytics.com/)
- [DJITelloPy - Tello Drone Python SDK](https://github.com/damiafuentes/DJITelloPy)

