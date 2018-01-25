from matplotlib import pyplot as plt

import cv2
import numpy as np
import pdb


img_full = cv2.imread('00608r.jpg', 0)

# crop the original image to remove outer white border
t, b = 10, 7
l, r = 2, 2
img = img_full[t:img_full.shape[0] - b, l:img_full.shape[1] - r]

img_h, img_w = img.shape
split_h = int(img_h / 3)

img_b = img.copy()[:split_h, :]
img_g = img.copy()[split_h:split_h * 2, :]
img_r = img.copy()[split_h * 2:split_h * 3, :]

# pdb.set_trace()

img_bgr = np.zeros((split_h, img_w, 3), 'uint8')

# for i in range(3):
img_bgr[:, :, 0] = img_b
img_bgr[:, :, 1] = img_g
img_bgr[:, :, 2] = img_r

plt.subplot(141), plt.imshow(img_b,'gray'), plt.title('Blue')
plt.subplot(142), plt.imshow(img_g,'gray'), plt.title('Green')
plt.subplot(143), plt.imshow(img_r,'gray'), plt.title('Red')
plt.subplot(144), plt.imshow(img_bgr,'gray'), plt.title('BGR')

plt.show()
