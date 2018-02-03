from image_read_funcs import split_image_to_bgr
from matplotlib import pyplot as plt
from plot_funcs import plot_1x2

import argparse
import cv2
import numpy as np
import sys


def blur_and_pyr_up(img, kernel, max_width):
    '''
    Blurrs and moves and image up in the image pyramid

    Args:
        img: array - image to be blurred
        filter: array - filter used to blur
        max_width: int - maximum width of the image in the upper most level
                         of the pyramid

    Returns:
        blurred: array - blurred image
    '''

    h, w, c = img.shape
    max_levels = int(w / max_width)
    print('Image width: {} \t Max allowed width: {}'.format(w, max_width))
    print('Max levels in the image pyramid: {}'.format(max_levels))

    blurred = img
    for i in range(max_levels):
        print('processing level {}'.format(i))
        resized = cv2.resize(blurred, (0, 0), fx=0.5, fy=0.5)
        blurred = cv2.filter2D(resized, -1, kernel)
        plot_1x2(img, blurred, 'Original', 'Resized Image')

    return blurred


def multi_scale_align(img):

    kernel = np.ones((3, 3), np.float32) / 9
    max_width = 500
    pyr_up = blur_and_pyr_up(img, kernel, max_width)

    return pyr_up


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            'Aligns images using multi-scale method.'))
    parser.add_argument(
        'file',
        nargs='?',
        default='images/01164v.jpg',
        help='specify the path to gps log, default=images/01164v.jpg')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        # parser.print_help()
        # print('\nno image specfied, using default image.. \n')
        args.file = 'images/01164v.jpg'

    img_name = args.file
    img = cv2.imread(img_name, 0)
    img_bgr = split_image_to_bgr(img)

    algnd_img = multi_scale_align(img_bgr)

    plot_1x2(img_bgr, algnd_img, 'Original', 'Resized Image')
    plt.show()
