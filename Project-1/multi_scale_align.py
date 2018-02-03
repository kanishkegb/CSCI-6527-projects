from image_read_funcs import split_image_to_bgr
from matplotlib import pyplot as plt
from plot_funcs import plot_1x2

import argparse
import cv2
import numpy as np
import sys


def blur_and_pyr(img, kernel, level, max_level):
    '''
    Blurrs and moves and image up in the image pyramid

    Args:
        img: array - image to be blurred
        filter: array - filter used to blur
        level: int - cuurent level in the image pyramid
        max_level: int - maximum level of the pyramid

    Returns:
        blurred: array - blurred image
    '''

    if level == max_level:
        img_algnd, roll_g, roll_r = brute_force_align(img)

        return img_algnd, roll_g, roll_r


    blurred = img
    for i in range(max_levels):
        print('processing level {}'.format(i))
        resized = cv2.resize(blurred, (0, 0), fx=0.5, fy=0.5)
        blurred = cv2.filter2D(resized, -1, kernel)
        plot_1x2(img, blurred, 'Original', 'Resized Image')

    return blurred


def multi_scale_align(img, max_width=200):
    '''
    Blurrs and moves and image up in the image pyramid

    Args:
        img: array - image to be aligned
        max_width: int - maximum width of the image in the upper most level
                         of the pyramid

    Returns:
        img_algnd: array - aligned image
    '''

    h, w, c = img.shape
    max_level = int(w / max_width)

    print('Image width: {} \t Max allowed width: {}'.format(w, max_width))
    print('Max levels in the image pyramid: {}'.format(max_level))

    kernel = np.ones((3, 3), np.float32) / 9

    level = 0
    img_algnd = blur_and_pyr(img, kernel, level, max_level)

    return img_algnd


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
