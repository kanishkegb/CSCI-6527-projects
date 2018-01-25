import numpy as np
import cv2

img = cv2.imread('00608r.jpg', 0)

cv2.imshow('Image', img)
key = cv2.waitKey(0) & 0xFF
