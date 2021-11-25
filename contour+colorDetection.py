import cv2
import numpy as np


def nothing(x):
    # any operation
    pass


cap = cv2.imread('plate.png')


cv2.namedWindow('Trackbars', cv2.WINDOW_NORMAL)
cv2.createTrackbar("Lower-Canny", "Trackbars", 150, 300, nothing)
cv2.createTrackbar("Upper-Canny", "Trackbars", 200, 300, nothing)
font = cv2.FONT_HERSHEY_COMPLEX

l_c = cv2.getTrackbarPos("Lower-Canny", "Trackbars")
u_c = cv2.getTrackbarPos("Upper-Canny", "Trackbars")

frameCanny = cv2.Canny(cap,l_c,u_c)

contours, _ = cv2.findContours(frameCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if area > 400:
        cv2.drawContours(cap, [approx], 0, (0, 0, 0), 5)

        if len(approx) == 3:
            cv2.putText(cap, "Triangle", (x, y), font, 1, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(cap, "Rectangle", (x, y), font, 1, (0, 0, 0))
        elif 7 < len(approx) < 20:
            cv2.putText(cap, "Circle", (x, y), font, 1, (0, 0, 0))

# ============================================================================

# Convert the imageFrame in
# BGR(RGB color space) to
# HSV(hue-saturation-value)
# color space
hsvFrame = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

# Set range for red color and
# define mask
red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

# Set range for white color and
# define mask
white_lower = np.array([0, 0, 200], np.uint8)
white_upper = np.array([0, 0, 255], np.uint8)
white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

# Set range for green color and
# define mask
green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

# Set range for blue color and
# define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

# Morphological Transform, Dilation
# for each color and bitwise_and operator
# between imageFrame and mask determines
# to detect only that particular color
kernal = np.ones((5, 5), "uint8")

# For red color
red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(cap, cap,
                            mask=red_mask)

# For white color
white_mask = cv2.dilate(white_mask, kernal)
res_white = cv2.bitwise_and(cap, cap,
                            mask=white_mask)

# For green color
green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(cap, cap,
                            mask=green_mask)

# For blue color
blue_mask = cv2.dilate(blue_mask, kernal)
res_blue = cv2.bitwise_and(cap, cap,
                            mask=blue_mask)

# Creating contour to track red color
contours, hierarchy = cv2.findContours(red_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        cap = cv2.rectangle(cap, (x, y),
                                    (x + w, y + h),
                                    (0, 0, 255), 2)

        cv2.putText(cap, "Red", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))

# Creating contour to track white color
contours, hierarchy = cv2.findContours(white_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        cap = cv2.rectangle(cap, (x, y),
                                    (x + w, y + h),
                                    (255, 255, 255), 2)

        cv2.putText(cap, "White", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (255, 255, 255))

# Creating contour to track green color
contours, hierarchy = cv2.findContours(green_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        cap = cv2.rectangle(cap, (x, y),
                                    (x + w, y + h),
                                    (0, 255, 0), 2)

        cv2.putText(cap, "Green", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0))

# Creating contour to track blue color
contours, hierarchy = cv2.findContours(blue_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        cap = cv2.rectangle(cap, (x, y),
                                    (x + w, y + h),
                                    (255, 0, 0), 2)

        cv2.putText(cap, "Blue", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 0, 0))

# Program Termination
cv2.imshow("Multiple Color Detection in Real-TIme", cap)


cv2.imshow("Grey", frameCanny)
cv2.imshow("Image",cap)

key = cv2.waitKey(100)
cv2.waitKey(0)
cv2.destroyAllWindows()