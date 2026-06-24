import cv2
import cv2.aruco as aruco

dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# Create marker
marker = aruco.generateImageMarker(dictionary, 0, 400)

# Add a white border around it
marker = cv2.copyMakeBorder(
    marker,
    100, 100, 100, 100,
    cv2.BORDER_CONSTANT,
    value=255
)

cv2.imwrite("marker0.png", marker)

print("Marker generated successfully!")