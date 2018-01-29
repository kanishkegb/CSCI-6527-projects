from matplotlib import pyplot as plt

import cv2
import numpy as np


def plot_bgr(img_b, img_g, img_r, img_bgr):
    '''
    Plots 4x1 subplots of each channel and the combined figure.

    Args:
        img_b, img_g, img_r: arrays - images on each channel - blue, green, red
        img_bgr = array - combined image of all three channels, in BGR

    Returns:
        None
    '''

    # cv2 uses BGR, but plt uses RGB
    plt.figure()
    plt.subplot(141)
    plt.imshow(cv2.cvtColor(img_b, cv2.COLOR_BGR2RGB))
    plt.title('Blue')
    plt.xticks([]), plt.yticks([])

    plt.subplot(142)
    plt.imshow(cv2.cvtColor(img_g, cv2.COLOR_BGR2RGB))
    plt.title('Green')
    plt.xticks([]), plt.yticks([])

    plt.subplot(143)
    plt.imshow(cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB))
    plt.title('Red')
    plt.xticks([]), plt.yticks([])

    plt.subplot(144)
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title('BGR')
    plt.xticks([]), plt.yticks([])

    return


def plot_fig(img):
    '''
    Plot single image in BGR colorspace

    Args:
        img: array - image to be plotted

    Returns:
        None
    '''

    plt.figure()
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Image')
    plt.xticks([]), plt.yticks([])

    return
