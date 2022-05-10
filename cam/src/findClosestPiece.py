#!/usr/bin/env python3

from re import M, T
import cv2
import numpy as np
from math import ceil
from math import sqrt


def nothing(x):
    # any operation
    pass

# Entry : List
# Output : Same list without duplication element
def duplicates_remove(list):
    for i in list:
        if i in list:
            list.remove(i)
    return list
    
    
# ============================================================
# Input : Image of the objects to detect
# Output : [ shape , color , x_center , y_center , ID]
def findInfo(image):

    font = cv2.FONT_HERSHEY_COMPLEX
    frameCanny = cv2.Canny(image,150,300)


    contours, _ = cv2.findContours(frameCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    liste = []
    type = 0
    id = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(image, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3: # Triangle
                # WARNING the center recovered for the triangle is the center of the rectangle surrounding the triangle, not the center of the triangle
                cv2.putText(image, "Triangle", (x, y), font, 1, (0, 0, 0))
                type = 2

            elif len(approx) == 4: # Square
                cv2.putText(image, "Rectangle", (x, y), font, 1, (0, 0, 0))
                type = 1
            elif len(approx) == 10:
                cv2.putText(image, "Star", (x, y), font, 1, (0, 0, 0))
                type = 4
            elif 5 < len(approx) < 20: # Circle
                cv2.putText(image, "Circle", (x, y), font, 1, (0, 0, 0))
                type = 3

            x,y,w,h = cv2.boundingRect(cnt) # offsets - with this you get 'mask'
            #cv2.imshow('cutted contour',frame[y:y+h,x:x+w])
            pixel_average = np.array(cv2.mean(image[y:y+h,x:x+w])).astype(np.uint8)
            #print('Average color (BGR): ',pixel_average)
            color = ["Blue", "Green","Red"]
            L = list(pixel_average)
            couleur = color[L.index(max(pixel_average))]
            # Computation of the center of the rectangle
            x_c = int(ceil(x+0.5*w))
            y_c = int(ceil(y+0.5*h))
            cv2.circle(image, (x_c,y_c), radius=5, color=(255, 255, 255), thickness=-1)

            # We save all the information for each element
            liste.append([type,couleur,x_c,y_c])

    # We add the id of each element
    id = 0
    L_data = duplicates_remove(liste)
    for i in L_data :
        i.append(id)
        id+=1

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)

    print(L_data)

    return L_data



frame = cv2.imread("/home/kevin/catkin_ws/src/cam/image/figures.png")

# ============================================================
# Input : 2x2 list - Coordinates of the end effector (x,y)
# Output : Info [ shape , color , x_center , y_center , ID] of the closest element
def findClosestPiece(coordinates,shape,color):
    
    objectInfo = findInfo(frame)    

    candidate = []
    for object in objectInfo :
        if object[1]==color and object[0]==shape :
            candidate.append(object)

    print(candidate)

    dist = []
    for object in candidate:
        dist.append(sqrt((object[2]-coordinates[0])**2+(object[3]-coordinates[1])**2))

    return candidate[dist.index(min(dist))][2:4]

# ============================================================O

print(findClosestPiece([0,0],1,'Red'))