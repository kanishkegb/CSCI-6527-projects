from single_scale_align import brute_force_align
from crop_funcs import crop_aligned_image
from image_read_funcs import split_image_to_bgr
from matplotlib import pyplot as plt
from plot_funcs import plot_1x2

import argparse
import cv2
import numpy as np
import sys


def roll_gr_from_coarse(img, coarse_g, coarse_r):
    '''
    Rolls G and R layers of a BGR image by the coarse roll values calculated
    at the upper level of the image pyramid

    Args:
        img: aray - image to be rolled
        coarse_g: int tuple - pixel roll for aligning G channel calculated
                  at upper level of image pyramid
        coarse_r: int tuple - pixel roll for aligning R channel calculated
                  at upper level of image

    Returns:
        img_coarse: aray - aligned image
        coarse_g: int tuple - pixels rolled for aligning G channel
        coarse_r: int tuple - pixels rolled for aligning R channel
    '''

    # scale coarse roll values from previous level
    coarse_g = (coarse_g[0] * 2, coarse_g[1] * 2)
    coarse_r = (coarse_r[0] * 2, coarse_r[1] * 2)
    # import pdb; pdb.set_trace()

    h, w, c = img.shape
    img_coarse = np.zeros((h, w, 3), 'uint8')
    img_coarse[:, :, 0] = img[:, :, 0]
    img_coarse[:, :, 1] = np.roll(img[:, :, 1], coarse_g, (0, 1))
    img_coarse[:, :, 2] = np.roll(img[:, :, 2], coarse_r, (0, 1))

    return img_coarse, coarse_g, coarse_r


def roll_gr(img, roll_g, roll_r):
    '''
    Rolls G and R layers of a BGR image by the given roll values

    Args:
        img: aray - image to be rolled
        coarse_g: int tuple - pixel roll for aligning G channel calculated
                  at upper level of image pyramid
        coarse_r: int tuple - pixel roll for aligning R channel calculated
                  at upper level of image pyramid
    '''

    h, w, c = img.shape

    img_rolled = np.zeros((h, w, 3), 'uint8')
    img_rolled[:, :, 0] = img[:, :, 0]
    img_rolled[:, :, 1] = np.roll(img[:, :, 1], roll_g, (0, 1))
    img_rolled[:, :, 2] = np.roll(img[:, :, 2], roll_r, (0, 1))

    return img_rolled


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
        img_algnd, roll_g, roll_r = brute_force_align(img, 20)
        # plot_1x2(img, img_algnd, 'Original', 'Resized Image')

        return roll_g, roll_r

    resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    blurred = cv2.filter2D(resized, -1, kernel)
    # blurred = resized
    up_g, up_r = blur_and_pyr(blurred, kernel, level + 1, max_level)
    # plot_1x2(img, blurred, 'Original', 'Resized Image')

    # fine tune based on the coarse tuning
    img_coarse, coarse_g, coarse_r = roll_gr_from_coarse(img, up_g, up_r)
    img_algnd, fine_g, fine_r = brute_force_align(img_coarse, 2)
    # import pdb; pdb.set_trace()

    roll_g = (coarse_g[0] + fine_g[0], coarse_g[1] + fine_g[1])
    roll_r = (coarse_r[0] + fine_r[0], coarse_r[1] + fine_r[1])

    return roll_g, roll_r


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
    max_level = int(np.log2(w / max_width)) + 1
    # import pdb; pdb.set_trace()

    print('Image width: {} \t Max allowed width: {}'.format(w, max_width))
    print('Max levels in the image pyramid: {}'.format(max_level))

    kernel = np.ones((3, 3), np.float32) / 9

    level = 0
    roll_g, roll_r = blur_and_pyr(img, kernel, level, max_level)
    img_algnd = roll_gr(img, roll_g, roll_r)

    print('\nGreen: h {}, w {}'.format(roll_g[0], roll_g[1]))
    print('Red: h {}, w {}\n'.format(roll_r[0], roll_r[1]))

    return img_algnd, roll_g, roll_r


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
        parser.print_help()
        print('\nno image specfied, using default image.. \n')
        args.file = 'images/01164v.jpg'

    img_name = args.file
    img = cv2.imread(img_name, 0)
    img_bgr = split_image_to_bgr(img)

    algnd_img, roll_g, roll_r = multi_scale_align(img_bgr)
    cropped_image = crop_aligned_image(algnd_img, roll_g, roll_r)

    plot_1x2(img_bgr, algnd_img, 'Original', 'Aligned Image')
    plot_1x2(algnd_img, cropped_image, 'Aligned Image', 'Cropped Image')
    plt.show()
