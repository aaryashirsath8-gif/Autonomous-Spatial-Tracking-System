### Autonomous Spatial Tracking System



#### Project Overview:

###### This project uses OpenCV and ArUco markers to perform real-time spatial tracking.



#### Features:

1. ###### &#x20;Real-time webcam tracking
2. ###### &#x20;ArUco marker detection
3. ###### &#x20;Marker centroid calculation
4. ###### &#x20;Position error calculation
5. ###### &#x20;Directional commands:

###### 

* ###### &#x20;  MOVE LEFT
* ###### &#x20;  MOVE RIGHT
* ###### &#x20;  MOVE UP
* ###### &#x20;  MOVE DOWN
* ###### &#x20;  APPROACH
* ###### &#x20;  LOCK ENGAGED



#### Technologies Used:



* ###### &#x20;Python
* ###### &#x20;OpenCV
* ###### &#x20;NumPy



#### How to Run:

###### Install dependencies

###### pip install opencv-contrib-python numpy



#### Run:

###### python main.py

#### 

#### Output:

###### The system detects the ArUco marker and generates tracking commands based on its position relative to the center of the camera frame.



