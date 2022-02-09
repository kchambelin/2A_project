import cv2
import numpy as np
from math import ceil


def nothing(x):
    # any operation
    pass

img = cv.imread(cv.samples.findFile("figures.png"))


cv.imshow("Display window", img)
k = cv.waitKey(0)