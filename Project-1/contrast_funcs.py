import cv2
import numpy as np


def adjust_contrast(img):
    '''
    Adjust the contrast of the image by maping min and max values to 0 and 255
    respectively, for each layer.

    Args:
        img: array - image to be adjusted

    Returns:
        img: array - image with adjusted contrast
    '''

    for i in range(3):
        layer = img[:, :, i]
        img[:, :, i] = unify_contast(layer)

    return img


def unify_contast(layer):
    '''
    Maps the min value and max value to 0 and 255 of a given image layer.

    Args:
        layer: array - layer to be adjusted

    Returns:
        high_set: array - adjusted layer
    '''

    low = np.min(layer)
    low_set = layer - low

    high = np.max(low_set)
    high_set = low_set / high * 255

    print('Layer - min {}, max {}'.format(low, high))

    return high_set


if __name__ == '__main__':
    img = cv2.imread('images/lakeandballoon.jpg', 1)
    contr_image = adjust_contrast(img)
