from crop_funcs import detect_edges

import numpy as np


def split_image_to_bgr(img_full):
    '''
    Reads image, crops it, and split it into color layers and returns as a
    single BGR image

    Args:
        img_full: array - image with 3x1 B, G, and R layes

    Returns:
        img_bgr: array - standard BGR image
    '''

    # crop the original image to remove outer white border
    t, b, l, r = detect_edges(img_full)
    img = img_full[t:b, l:r]

    img_h, img_w = img.shape
    split_h = int(img_h / 3)

    img_bgr = np.zeros((split_h, img_w, 3), 'uint8')
    img_bgr[:, :, 0] = img[:split_h, :]
    img_bgr[:, :, 1] = img[split_h:split_h * 2, :]
    img_bgr[:, :, 2] = img[split_h * 2:split_h * 3, :]

    return img_bgr
