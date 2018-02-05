import cv2
import numpy as np


def adjust_contrast(img):

    for i in range(3):
        layer = img[:, :, i]
        img[:, :, i] = unify_contast(layer)

    return img


def unify_contast(layer):
    low = np.min(layer)
    low_set = layer - low

    high = np.max(low_set)
    high_set = low_set / high * 255

    print('Layer - min {}, max {}'.format(low, high))

    return high_set

if __name__ == '__main__':
    img = cv2.imread('images/lakeandballoon.jpg', 1)
    contr_image = adjust_contrast(img)
