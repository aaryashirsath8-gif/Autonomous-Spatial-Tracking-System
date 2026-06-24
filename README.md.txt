Autonomous Spatial Tracking System

Project Overview:
This project uses OpenCV and ArUco markers to perform real-time spatial tracking.

Features:
 1) Real-time webcam tracking
 2) ArUco marker detection
 3) Marker centroid calculation
 4) Position error calculation
 5) Directional commands:
     MOVE LEFT
     MOVE RIGHT
     MOVE UP
     MOVE DOWN
     APPROACH
     LOCK ENGAGED

Technologies Used:
1) Python
2) OpenCV
3) NumPy

How to Run:
Install dependencies
pip install opencv-contrib-python numpy

Run:
python main.py

Output:
The system detects the ArUco marker and generates tracking commands based on its position relative to the center of the camera frame.