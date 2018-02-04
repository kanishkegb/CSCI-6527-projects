import cv2
import numpy as np
# import pdb


def align_im(img1, img2, roll_lim=15):
    '''
    Aligns image 2 with image 1

    Args:
        img1: array - reference image
        img2: array - image to be aligned with img1
        roll_lim: int - pixel window to check for [default=15]

    Returns:
        aligned_im2: array - aligned img2
    '''

    min_err = np.inf
    min_h, min_w = 0, 0
    for h in range(-roll_lim, roll_lim, 1):
        for w in range(-roll_lim, roll_lim, 1):
            im2 = np.roll(img2, (h, w), (0, 1))
            err = calc_error(img1, im2)

            if err < min_err:
                min_err = err
                min_h, min_w = h, w

    # print('Roll: h {}, w {}'.format(min_h, min_w))
    aligned_im2 = np.roll(img2, (min_h, min_w), (0, 1))

    return aligned_im2, (min_h, min_w)


def calc_error(img1, img2):
    '''
    Calculates the array between img1 and img2

    Args:
        img1, img2: arrays - images to check the error for

    Returns:
        err: int - error value
    '''

    # ignore the borders
    h, w = img1.shape
    t = int(0.1 * h)
    l = int(0.1 * w)

    im1 = img1[t:-t, l:-l]
    im2 = img2[t:-t, l:-l]

    err = np.sum(np.power(im1 / np.max(im1) - im2 / np.max(im2), 2))

    return err


if __name__ == '__main__':
    img_full = cv2.imread('images/10131v.jpg', 0)
