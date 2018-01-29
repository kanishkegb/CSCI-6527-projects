from align_funcs import detect_edges, align_im
from matplotlib import pyplot as plt
from plot_funcs import plot_bgr, plot_fig

import cv2
import numpy as np

img_full = cv2.imread('images/00125v.jpg', 0)

# crop the original image to remove outer white border
t, b, l, r = detect_edges(img_full)
img = img_full[t:b, l:r]
# img = img_full

img_h, img_w = img.shape
split_h = int(img_h / 3)

img_bgr = np.zeros((split_h, img_w, 3), 'uint8')
img_bgr[:, :, 0] = img[:split_h, :]
img_bgr[:, :, 1] = img[split_h:split_h * 2, :]
img_bgr[:, :, 2] = img[split_h * 2:split_h * 3, :]

img_algnd = np.zeros((split_h, img_w, 3), 'uint8')
img_algnd[:, :, 0] = img_bgr[:, :, 0]
img_algnd[:, :, 1] = align_im(img_bgr[:, :, 0], img_bgr[:, :, 1])
img_algnd[:, :, 2] = align_im(img_bgr[:, :, 0], img_bgr[:, :, 2])

# img_algnd[:, :, 0] = np.roll(img_bgr[:, :, 0], (4, -1), (0, 1))
# img_algnd[:, :, 1] = np.roll(img_bgr[:, :, 1], (0, 0), (0, 1))
# img_algnd[:, :, 2] = np.roll(img_bgr[:, :, 2], (-5, -2), (0, 1))

# plot_fig(img_bgr_raw)
plot_fig(img_algnd)
# figManager = plt.get_current_fig_manager()
# figManager.window.showMaximized()

plt.show()
