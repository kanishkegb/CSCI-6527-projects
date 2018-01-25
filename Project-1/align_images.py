from matplotlib import pyplot as plt

import cv2
import numpy as np
import pdb


def plot_BGR(img_b, img_g, img_r, img_bgr):

    # cv2 uses BGR, but plt uses RGB
    plt.subplot(141)
    plt.imshow(cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB))
    plt.title('Blue')
    plt.xticks([]), plt.yticks([])

    plt.subplot(142)
    plt.imshow(cv2.cvtColor(img_g, cv2.COLOR_BGR2RGB))
    plt.title('Green')
    plt.xticks([]), plt.yticks([])

    plt.subplot(143)
    plt.imshow(cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB))
    plt.title('Red')
    plt.xticks([]), plt.yticks([])

    plt.subplot(144)
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title('BGR')
    plt.xticks([]), plt.yticks([])

    return


def plot_fig(img):
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title('Image')
    plt.xticks([]), plt.yticks([])


img_full = cv2.imread('images/00458u.jpg', 0)

# crop the original image to remove outer white border
t, b = 10, 7
l, r = 2, 2
img = img_full[t:img_full.shape[0] - b, l:img_full.shape[1] - r]

img_h, img_w = img.shape
split_h = int(img_h / 3)

img_b = np.zeros((split_h, img_w, 3), 'uint8')
img_g = np.zeros((split_h, img_w, 3), 'uint8')
img_r = np.zeros((split_h, img_w, 3), 'uint8')

img_b[:, :, 0] = img[:split_h, :]
img_g[:, :, 1] = img[split_h:split_h * 2, :]
img_r[:, :, 2] = img[split_h * 2:split_h * 3, :]

img_bgr = np.zeros((split_h, img_w, 3), 'uint8')
img_bgr[:, :, 0] = img_b[:, :, 0]
img_bgr[:, :, 1] = img_g[:, :, 1]
img_bgr[:, :, 2] = img_r[:, :, 2]

# plot_BGR(img_b, img_g, img_r, img_bgr)
plot_fig(img)
plt.show()
