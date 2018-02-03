from matplotlib import pyplot as plt
from plot_funcs import plot_fig

import cv2
import numpy as np
import pdb


def detect_edges(img):

    sobel_vertical = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    vertical = cv2.filter2D(img, -1, sobel_vertical)

    sobel_horizontal = sobel_vertical.T
    horizontal = cv2.filter2D(img, -1, sobel_horizontal)

    return vertical + horizontal


if __name__ == '__main__':

    img = cv2.imread('images/lakeandballoon.jpg', 0)
    edges = detect_edges(img)

    plt.imshow(edges)

    plt.xticks([]), plt.yticks([])
    plt.show()
