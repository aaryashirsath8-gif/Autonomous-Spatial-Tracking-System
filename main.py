import cv2
import cv2.aruco as aruco
import numpy as np

# -----------------------------
# Webcam Setup
# -----------------------------
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# -----------------------------
# ArUco Setup
# -----------------------------
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

detector = aruco.ArucoDetector(aruco_dict, parameters)

# Lock threshold
THRESHOLD = 10

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    h, w = frame.shape[:2]
    # Professional Header
    cv2.rectangle(frame, (0, 0), (w, 50), (40, 40, 40), -1)

    cv2.putText(
      frame,
      "AUTONOMOUS SPATIAL TRACKING SYSTEM",
      ( 15, 32),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.7,
      (255, 255, 255),
       2
    )

    center_x = w // 2
    center_y = h // 2

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect markers
    corners, ids, rejected = detector.detectMarkers(gray)

    # Draw center crosshair

    cv2.circle(frame, (center_x, center_y), 30, (0, 255, 0), 2)
    cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
 
    command = "SEARCHING..."

    # Marker count display
    marker_count = 0 if ids is None else len(ids)
    cv2.rectangle(frame, (10, 60), (200, 230), (50, 50, 50), -1)

    cv2.putText(
        frame,
        f"Markers Detected: {marker_count}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 255),
        2
    )

    if ids is not None and len(corners) > 0:
        cv2.putText(
        frame,
        f"Marker ID: {ids[0][0]}",
        (20, 210),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        1
    )
        
    for corner in corners:
        pts = corner.astype(int)
        cv2.polylines(frame, [pts], True, (0,255,0), 2)

        marker = corners[0][0]

        # Marker center
        cX = int(np.mean(marker[:, 0]))
        cY = int(np.mean(marker[:, 1]))

        # Draw centroid
        cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

        # Draw vector
        cv2.arrowedLine(
            frame,
            (center_x, center_y),
            (cX, cY),
            (255, 0, 0),
            2
        )

        # Error calculations
        error_x = cX - center_x
        error_y = cY - center_y

        # Marker area
        area = cv2.contourArea(marker.astype(np.float32))

        commands = []

        # Lock Condition
        if abs(error_x) <= THRESHOLD and abs(error_y) <= THRESHOLD:

            command = "LOCK ENGAGED"

        else:

            if error_x < -THRESHOLD:
                commands.append("MOVE LEFT")

            elif error_x > THRESHOLD:
                commands.append("MOVE RIGHT")

            if error_y < -THRESHOLD:
                commands.append("MOVE UP")

            elif error_y > THRESHOLD:
                commands.append("MOVE DOWN")

            # Distance guidance
            if area < 5000:
                commands.append("APPROACH")

            command = " | ".join(commands)

        # Display errors
        cv2.putText(
            frame,
            f"X Error: {error_x}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1
        )

        cv2.putText(
            frame,
            f"Y Error: {error_y}",
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1
        )

        cv2.putText(
            frame,
            f"Area: {int(area)}",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            1
        )

    # Command display

    if command == "LOCK ENGAGED":
        color = (0, 255, 0)

    elif command == "SEARCHING...":
        color = (0, 0, 255)

    else:
       color = (0, 255, 255)
    
    cv2.putText(
        frame,
        command,
        (20, h - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )
    status = "TRACKING TARGET" if ids is not None else "SEARCHING TARGET"

    cv2.putText(
       frame,
       f"SYSTEM STATUS : {status}",
       (20, h - 60),
       cv2.FONT_HERSHEY_SIMPLEX,
       0.8,
       (255, 255, 255),
       2
)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(
       frame,
       f"FPS : {int(fps)}",
       (w - 90, 32 ),
       cv2.FONT_HERSHEY_SIMPLEX,
       0.6,
       (255, 255, 255),
       2
    )
    cv2.imshow("Autonomous Spatial Tracking System", frame)
    

    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()