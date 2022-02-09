from re import T
import cv2
import numpy as np
from math import ceil


def nothing(x):
    # any operation
    pass

def duplicates_remove(list):
    for i in list:
        if i in list:
            list.remove(i)
    return list

frame = cv2.imread(cv2.samples.findFile("figures.png"))

font = cv2.FONT_HERSHEY_COMPLEX
frameCanny = cv2.Canny(frame,150,300)


contours, _ = cv2.findContours(frameCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
liste = []
type = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if area > 400:
        cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

        if len(approx) == 3: # Triangle
            # WARNING the center recovered for the triangle is the center of the rectangle surrounding the triangle, not the center of the triangle
            cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
            type = 2

        elif len(approx) == 4: # Square
            cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
            type = 1
        elif 5 < len(approx) < 20: # Circle
            cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))
            type = 3

        x,y,w,h = cv2.boundingRect(cnt) # offsets - with this you get 'mask'
        #cv2.imshow('cutted contour',frame[y:y+h,x:x+w])
        pixel_average = np.array(cv2.mean(frame[y:y+h,x:x+w])).astype(np.uint8)
        #print('Average color (BGR): ',pixel_average)
        color = ["Blue", "Green","Red"]
        L = list(pixel_average)
        couleur = color[L.index(max(pixel_average))]
        # Computation of the center of the rectangle
        x_c = ceil(x+0.5*w)
        y_c = ceil(y+0.5*h)
        cv2.circle(frame, (x_c,y_c), radius=5, color=(255, 255, 255), thickness=-1)
            
        liste.append([type,couleur,x_c,y_c])

print(duplicates_remove(liste))

cv2.imshow("Display window", frame)
k = cv2.waitKey(0)