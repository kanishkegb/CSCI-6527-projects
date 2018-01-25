import cv2
import numpy as np
import pdb


img = cv2.imread('00608r.jpg', 0)

img_h, img_w = img.shape

img_b = img.copy()[:int(img_h / 3), :]
img_g = img.copy()[int(img_h / 3):int(img_h * 2 / 3), :]
img_r = img.copy()[int(img_h * 2 / 3):, :]

pdb.set_trace()

cv2.imshow('Image', img)
key = cv2.waitKey(0) & 0xFF
