import cv2
import numpy as np

cap = cv2.VideoCapture("C:\\Users\\ramaz\\OneDrive\\Masaüstü\OpenCV\\9. OpenCV  Contours, Convex Hull, Convexity Defects\\4.2 dog.mp4.mp4")

while 1:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()