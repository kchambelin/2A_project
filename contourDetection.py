import cv2
import numpy as np


def nothing(x):
    # any operation
    pass


cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 526)


cv2.namedWindow('Trackbars', cv2.WINDOW_NORMAL)
cv2.createTrackbar("Lower-Canny", "Trackbars", 150, 300, nothing)
cv2.createTrackbar("Upper-Canny", "Trackbars", 200, 300, nothing)
font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = cap.read()

    l_c = cv2.getTrackbarPos("Lower-Canny", "Trackbars")
    u_c = cv2.getTrackbarPos("Upper-Canny", "Trackbars")

    frameCanny = cv2.Canny(frame,l_c,u_c)

    contours, _ = cv2.findContours(frameCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
            elif 10 < len(approx) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("Grey", frameCanny)
    cv2.imshow("Image",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()