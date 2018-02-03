from align_funcs import align_im
from image_read_funcs import split_image_to_bgr
from matplotlib import pyplot as plt
from plot_funcs import plot_aligned

import cv2
import numpy as np


def brute_force_align(img):
    '''
    Aligns each layer of an image in BGR colorspace with the B layer

    Args:
        img: array - image in BGR colorspace that needs to be aligned

    Returns:
        img_algnd: aray - aligned image
        roll_g: int tuple - pixels rolled for aligning green channel
        roll_r: int tuple - pixels rolled for aligning red channel
    '''

    img_bgr = split_image_to_bgr(img)

    h, w, c = img_bgr.shape

    img_algnd = np.zeros((h, w, 3), 'uint8')
    img_algnd[:, :, 0] = img_bgr[:, :, 0]
    img_algnd[:, :, 1], roll_g = align_im(img_bgr[:, :, 0], img_bgr[:, :, 1])
    img_algnd[:, :, 2], roll_r = align_im(img_bgr[:, :, 0], img_bgr[:, :, 2])

    return img_algnd, roll_g, roll_r


if __name__ == '__main__':

    img = cv2.imread('images/01164v.jpg', 0)
    img_algnd, roll_g, roll_r = brute_force_align(img)

    # img_algnd[:, :, 1] = np.roll(img_bgr[:, :, 1], (-22, 6), (0, 1))
    # img_algnd[:, :, 2] = np.roll(img_bgr[:, :, 2], (-43, 32), (0, 1))

    # plot_fig(img_bgr_raw)
    # plot_fig(img_algnd)
    plot_aligned(img_algnd, roll_g, roll_r)
    # plot_aligned(img_algnd, (-22, 6), (-43, 32))
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    plt.show()
