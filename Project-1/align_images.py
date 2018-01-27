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


def align_bg(img_b, img_g):

    h, w = img_b.shape[:2]
    t = int(h / 3)
    b = int(h * 2 / 3)
    l = int(w / 3)
    r = int(w * 2 / 3)
    t, b = 0, -1
    l, r = 0, -1

    im1 = img_b[t:b, l:r, 0]
    im2 = img_g[t:b, l:r, 1]

    min_err = 1e100
    min_h_roll, min_w_roll = 0, 0
    for h_roll in range(-100, 100, 5):
        im2_h_roll = np.roll(im2, h_roll, axis=0)
        for w_roll in  range(-100, 100, 5):
            im2_w_roll = np.roll(im2_h_roll, w_roll, axis=1)
            err = np.sum(pow(im1 - im2_w_roll, 2))
            # print(err)
            if err < min_err:
                min_err = err
                min_h_roll, min_w_roll = h_roll, w_roll

    im2_h_roll = np.roll(img_g, min_h_roll, axis=0)
    im2_w_roll = np.roll(im2_h_roll, min_w_roll, axis=1)

    return im2_w_roll[:, :, 1]


def align_br(img_b, img_r):

    h, w = img_b.shape[:2]
    # t = int(h / 3)
    # b = int(h * 2 / 3)
    # l = int(w / 3)
    # r = int(w * 2 / 3)
    t, b = 50, -50
    l, r = 50, -50

    im1 = img_b[t:b, l:r, 0]
    im2 = img_r[t:b, l:r, 1]

    min_err = 1e100
    min_h_roll, min_w_roll = 0, 0
    for h_roll in range(-100, 100, 5):
        im2_h_roll = np.roll(im2, h_roll, axis=0)
        for w_roll in  range(-100, 100, 5):
            im2_w_roll = np.roll(im2_h_roll, w_roll, axis=1)
            err = np.sum(pow(im1 - im2_w_roll, 2))
            # print(err)
            if err < min_err:
                min_err = err
                min_h_roll, min_w_roll = h_roll, w_roll

    im2_h_roll = np.roll(img_r, min_h_roll, axis=0)
    im2_w_roll = np.roll(im2_h_roll, min_w_roll, axis=1)
    # pdb.set_trace()

    return im2_w_roll[:, :, 2]


if __name__ == '__main__':
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

    img_bgr_raw = np.zeros((split_h, img_w, 3), 'uint8')
    img_bgr_raw[:, :, 0] = img_b[:, :, 0]
    img_bgr_raw[:, :, 1] = img_g[:, :, 1]
    img_bgr_raw[:, :, 2] = img_r[:, :, 2]


    img_bgr = np.zeros((split_h, img_w, 3), 'uint8')
    img_bgr[:, :, 0] = img_b[:, :, 0]
    img_bgr[:, :, 1] = align_bg(img_b, img_g)
    img_bgr[:, :, 2] = align_br(img_b, img_r)
    # b_h_roll, b_w_roll = align_bg(img_b, img_g)

    plot_fig(img_bgr)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # plot_BGR(img_b, img_g, img_r, img_bgr)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # plot_fig(img_bgr_raw)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    plt.show()
