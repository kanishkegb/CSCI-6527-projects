from matplotlib import pyplot as plt
from fig_plots import plot_bgr, plot_fig

import cv2
import numpy as np
import pdb


def detect_edges(img):
    '''
    Detects the border of the image based on the difference of the white outer
    space and the black border.

    Args:
        img: array - image to be cropped

    Returns:
        t, b: int - top and bottom crop limits
        l, r: int - left and right crop limits
    '''

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
    '''
    Aligns green channel to blue channel

    Args:
        img_b: array - image of blue channel
        img_g: array - image of green channel

    Returns:
        im2_w_roll: array - aligned green channel
    '''

    h, w = img_b.shape[:2]
    t = int(h / 3)
    b = int(h * 2 / 3)
    l = int(w / 3)
    r = int(w * 2 / 3)
    t, b = 0, -1
    l, r = 0, -1

    im1 = img_b[t:b, l:r, 0]
    im2 = img_g[t:b, l:r, 1]

    h_roll, w_roll = find_min_err(im1, im2, 50)

    im2_h_roll = np.roll(img_g, h_roll, axis=0)
    im2_w_roll = np.roll(im2_h_roll, w_roll, axis=1)

    return im2_w_roll[:, :, 1]


def align_br(img_b, img_r):
    '''
    Aligns red channel to blue channel

    Args:
        img_b: array - image of blue channel
        img_r: array - image of red channel

    Returns:
        im2_w_roll: array - aligned red channel
    '''

    h, w = img_b.shape[:2]

    # ignore the borders
    t = int(0.2 * h)
    l = int(0.2 * w)
    im1 = img_b[t:-t, l:-l, 0]
    im2 = img_r[t:-t, l:-l, 2]

    h_roll, w_roll = find_min_err(im1, im2, 50)

    im2_h_roll = np.roll(img_r, h_roll, axis=0)
    im2_w_roll = np.roll(im2_h_roll, w_roll, axis=1)

    return im2_w_roll[:, :, 2]


def find_min_err(im1, im2, roll_lim=50):
    '''
    Calculates the number of pixels to be rolled along each axis such that the
    error between the compared figures is minimum

    Args:
        im1, im2: arrays - images to be compared
        roll_lim: int - roll window [default = 50 px]

    Returns:
        h_roll: int - pixels need to be rolled along height of the image
        w_roll:  int - pixels need to be rolled along width of the image
    '''

    min_err = 1e100
    min_h_roll, min_w_roll = 0, 0
    for h_roll in range(-roll_lim, roll_lim, 1):
        im2_h_roll = np.roll(im2, h_roll, axis=0)
        for w_roll in  range(-roll_lim, roll_lim, 1):
            im2_w_roll = np.roll(im2_h_roll, w_roll, axis=1)
            err = np.sum(pow(im1 - im2_w_roll, 2))
            if err < min_err:
                min_err = err
                min_h_roll, min_w_roll = h_roll, w_roll

    return min_h_roll, min_w_roll


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

    # plot_bgr(img_b, img_g, img_r, img_bgr)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # plot_fig(img_bgr_raw)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    plt.show()
