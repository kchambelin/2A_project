#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from re import M, T
import numpy as np
from math import ceil
from math import sqrt


class image_converter:

    def __init__(self):

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("camera1/image_raw",Image,self.callback)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows,cols,channels) = cv_image.shape
        if cols > 60 and rows > 60 :
            cv2.circle(cv_image, (50,50), 10, 255)
            findInfo(cv_image[365:440,240:325])

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

        if area > 150 and area < 250:
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
            elif 5 < len(approx): # Circle
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
            cv2.circle(image, (x_c,y_c), radius=3, color=(255, 255, 255), thickness=-1)

            # We save all the information for each element
            liste.append([type,couleur,x_c,y_c])

    # We add the id of each element
    id = 0
    L_data = duplicates_remove(liste)
    for i in L_data :
        i.append(id)
        id+=1


    L_pieces = []

    for piece in L_data:
        if piece[2] > 55 and piece[3] > 55 :
            L_pieces.append([piece[-1], piece[0], piece[1], 9])
        elif piece[2] > 55 and piece[3] < 20 :
            L_pieces.append([piece[-1], piece[0], piece[1], 3])

    print(L_pieces)
    liste_pos = ''
    for piece in L_pieces :
        liste_pos += str(piece[-1]) + ' '
    pub_main.publish(liste_pos)

    cv2.imshow("Display window", image)
    cv2.waitKey(0)

    return L_pieces




def callback(data):
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__=="__main__" :
    print('Cam here')
    rospy.init_node('findInfo', anonymous=True)
    pub_main = rospy.Publisher('cam_main', String, queue_size=10)
    rospy.Subscriber("main_cam", String, callback)
    rospy.spin()