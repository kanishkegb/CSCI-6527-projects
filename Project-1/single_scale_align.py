from align_funcs import align_im
from crop_funcs import crop_aligned_image
from image_read_funcs import split_image_to_bgr
from matplotlib import pyplot as plt
from plot_funcs import plot_aligned, plot_fig, plot_bgr_and_combined, plot_1x2

import argparse
import cv2
import numpy as np
import sys


def brute_force_align(img, roll_lim=15):
    '''
    Aligns each layer of an image in BGR colorspace with the B layer

    Args:
        img: array - image in BGR colorspace that needs to be aligned

    Returns:
        img_algnd: aray - aligned image
        roll_g: int tuple - pixels rolled for aligning G channel
        roll_r: int tuple - pixels rolled for aligning R channel
    '''

    h, w, c = img.shape

    img_algnd = np.zeros((h, w, 3), 'uint8')
    img_algnd[:, :, 0] = img[:, :, 0]
    img_algnd[:, :, 1], roll_g = align_im(img[:, :, 0], img[:, :, 1], roll_lim)
    img_algnd[:, :, 2], roll_r = align_im(img[:, :, 0], img[:, :, 2], roll_lim)

    print('\nGreen: h {}, w {}'.format(roll_g[0], roll_g[1]))
    print('Red: h {}, w {}'.format(roll_r[0], roll_r[1]))

    return img_algnd, roll_g, roll_r


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            'Aligns images using exhaustive search.'))
    parser.add_argument(
        'file',
        nargs='?',
        default='images/01164v.jpg',
        help='specify the path to gps log, default=images/01164v.jpg')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        args.file = 'images/01164v.jpg'
        print('\nno image specfied, using default image.. \n')

    img_name = args.file

    img = cv2.imread(img_name, 0)
    img_bgr = split_image_to_bgr(img)
    img_algnd, roll_g, roll_r = brute_force_align(img_bgr)

    cropped_image = crop_aligned_image(img_algnd, roll_g, roll_r)
    # plot_fig(img_bgr_raw)
    # plot_fig(img_algnd)
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    plot_bgr_and_combined(img_bgr[:, :, 0], img_bgr[:, :, 1],
                          img_bgr[:, :, 2], img_algnd)

    plot_1x2(img_algnd, cropped_image, 'Before', 'Cropped')
    plot_aligned(cropped_image, roll_g, roll_r)
    plt.show()
