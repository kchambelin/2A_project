import cv2
import numpy as np
from math import ceil


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
    liste = []
    rect = []
    i=0
    lst_intensities = []
    for cnt in contours:
        i += 1
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

                x,y,w,h = cv2.boundingRect(cnt) # offsets - with this you get 'mask'
                cv2.imshow('cutted contour',frame[y:y+h,x:x+w])
                pixel_average = np.array(cv2.mean(frame[y:y+h,x:x+w])).astype(np.uint8)
                #print('Average color (BGR): ',pixel_average)
                color = ["Blue", "Green","Red"]
                L = list(pixel_average)
                couleur = color[L.index(max(pixel_average))]
                print(couleur)
                # Computation of the center of the rectangle
                x_c = ceil(x+0.5*w)
                y_c = ceil(y+0.5*h)
                cv2.circle(frame, (x_c,y_c), radius=5, color=(0, 255, 0), thickness=-1)
                
                liste.append([1,couleur,x_c,y_c])

            elif 5 < len(approx) < 20:
                cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
            print (liste)
    cv2.imshow("Grey", frameCanny)
    cv2.imshow("Image",frame)

    key = cv2.waitKey(100)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()