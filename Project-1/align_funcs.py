import cv2
import numpy as np
# import pdb


def detect_edges(img):
    '''
    Detects the border of the image based on the difference of the white outer
    space and the black border.

    Args:
        img: array - image to be cropped

    Returns:
        t, b: int - top and bottom crop limits
        l, r: int - left and right crop limits
    '''

    h, w = img.shape

    black_threshold = 50
    counter_threshold = w * 0.8
    t, b = 0, 0
    l, r = 0, 0

    t, l = find_top_left(img, black_threshold, counter_threshold)
    b, r = find_bottom_right(img, black_threshold, counter_threshold)

    return t, b, l, r


def find_top_left(img, black_threshold, counter_threshold):
    '''
    Finds top left corner of the border

    Args:
        img: array - image with the border
        black_threshold: int - black cutoff value
        counter_threshold: int - number of continous pixels to be checked
                                 for black color
    '''

    h, w = img.shape

    tl_found = 0
    for i in range(h):
        t_counter = 0
        l_found = 0
        for j in range(w):
            if img[i, j] < black_threshold:
                t_counter += 1
                if not l_found:
                    l_found = 1
                    l = j
            else:
                t_counter

            if t_counter > counter_threshold:
                t = i
                tl_found = 1
                break

        if tl_found:
            break

    return t, l


def find_bottom_right(img, black_threshold, counter_threshold):
    '''
    Finds bottom right corner of the border

    Args:
        img: array - image with the border
        black_threshold: int - black cutoff value
        counter_threshold: int - number of continous pixels to be checked
                                 for black color
    '''

    h, w = img.shape

    br_found = 0
    for i in range(h - 1, 0, -1):
        b_counter = 0
        r_found = 0
        for j in range(w - 1, 0, -1):
            if img[i, j] < black_threshold:
                b_counter += 1
                if not r_found:
                    r_found = 1
                    r = j
            else:
                b_counter

            if b_counter > counter_threshold:
                b = i
                br_found = 1
                break

        if br_found:
            break

    return b, r

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

    print('Roll: h {}, w {}'.format(min_h, min_w))
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


def digitize_layer(img, threshold=30):

    h, w = img.shape
    img_01 = np.zeros((h, w), 'uint8')
    for i in range(h):
        for j in range(w):
            if img[i, j] > threshold:
                img_01[i, j] = 255

    return img_01


def digitize_image(img_b, img_g, img_r):

    h, w = img_b.shape
    img_01 = np.zeros((h, w, 3), 'uint8')
    img_01[:, :, 0] = digitize_layer(img_b[:, :, 0])
    img_01[:, :, 1] = digitize_layer(img_g[:, :, 1])
    img_01[:, :, 2] = digitize_layer(img_r[:, :, 2])

    return img_01


if __name__ == '__main__':
    img_full = cv2.imread('images/10131v.jpg', 0)
