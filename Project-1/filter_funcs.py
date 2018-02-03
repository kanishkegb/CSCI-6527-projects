from matplotlib import pyplot as plt
from plot_funcs import plot_1x2

import cv2
import numpy as np
import pdb


def detect_edges(img):

    sobel_vertical = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    vertical = cv2.filter2D(img, -1, sobel_vertical)

    sobel_horizontal = sobel_vertical.T
    horizontal = cv2.filter2D(img, -1, sobel_horizontal)

    return vertical + horizontal


def blur_and_pyr_up(img, kernel):
    '''
    Blurrs and moves and image up in the image pyramid

    Args:
        img: array - image to be blurred
        filter: array - filter used to blur

    Returns:
        blurred: array - blurred image
    '''

    blurred = cv2.filter2D(img, -1, kernel)

    return blurred


if __name__ == '__main__':

    img = cv2.imread('images/lakeandballoon.jpg', 1)
    # edges = detect_edges(img)
    #
    # plt.imshow(edges)
    #
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    kernel = np.ones((3, 3), np.float32) / 9
    pyr_up = blur_and_pyr_up(img, kernel)

    plot_1x2(img, pyr_up, 'Original', 'Resized Image')
    # cv2.imshow("Image", pyr_up)
    # key = cv2.waitKey(0) & 0xFF
