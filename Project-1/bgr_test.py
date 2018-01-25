from matplotlib import pyplot as plt

import cv2
import numpy as np
import pdb


img = cv2.imread('images/lakeandballoon.jpg', 1)

img_h, img_w, img_ch = img.shape

img_b = img.copy()[:, :, 0]
img_g = img.copy()[:, :, 1]
img_r = img.copy()[:, :, 2]

img_bgr = np.zeros((img_h, img_w, 3), 'uint8')

img_bgr[:, :, 0] = img_b
img_bgr[:, :, 1] = img_g
img_bgr[:, :, 2] = img_r

cv2.imshow("Image", img_bgr)
key = cv2.waitKey(0) & 0xFF
