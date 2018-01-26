from matplotlib import pyplot as plt

import cv2
import numpy as np
import pdb


def plot_BGR(img_b, img_g, img_r, img_bgr):

    # cv2 uses BGR, but plt uses RGB
    plt.figure()
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
    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Image')
    plt.xticks([]), plt.yticks([])


def detect_edges(img):

    h, w = img.shape

    black_threshold = 50
    counter_threshold = w * 0.8
    t, b = 0, 0
    l, r = 0, 0

    tl_found = 0
    for i in range(h):
        t_counter = 0
        l_found = 0
        for j in range(w):
            if img[i, j] < black_threshold:
                t_counter += 1
                if not l_found:
                    l_found = 1
                    l = j
            else:
                t_counter

            if t_counter > counter_threshold:
                t = i
                tl_found = 1
                break

        if tl_found:
            break

    br_found = 0
    for i in range(h - 1, 0, -1):
        b_counter = 0
        r_found = 0
        for j in range(w - 1, 0, -1):
            if img[i, j] < black_threshold:
                b_counter += 1
                if not r_found:
                    r_found = 1
                    r = j
            else:
                b_counter

            if b_counter > counter_threshold:
                b = i
                br_found = 1
                break

        if br_found:
            break

    return t, b, l, r



img_full = cv2.imread('images/01597v.jpg', 0)

# crop the original image to remove outer white border
t, b, l, r = detect_edges(img_full)
img = img_full[t:b, l:r]

# plt.imshow(img)
# plt.show()

# pdb.set_trace()

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

plot_BGR(img_b, img_g, img_r, img_bgr)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plot_fig(img_bgr)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()
