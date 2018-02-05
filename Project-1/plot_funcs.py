from matplotlib import pyplot as plt

import cv2
# import numpy as np


def plot_bgr_and_combined(img_b, img_g, img_r, img_bgr):
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
    plt.imshow(img_b, cmap='gray')
    plt.title('Blue')
    plt.xticks([]), plt.yticks([])

    plt.subplot(142)
    plt.imshow(img_g, cmap='gray')
    plt.title('Green')
    plt.xticks([]), plt.yticks([])

    plt.subplot(143)
    plt.imshow(img_r, cmap='gray')
    plt.title('Red')
    plt.xticks([]), plt.yticks([])

    plt.subplot(144)
    plot_bgr(img_bgr)
    plt.title('BGR')
    plt.xticks([]), plt.yticks([])

    return


def plot_aligned(img, roll_g, roll_r):
    '''
    Plot single image in BGR colorspace

    Args:
        img: array - image to be plotted
        roll_g: int tuple - pixels rolled for aligning green channel
        roll_r: int tuple - pixels rolled for aligning red channel

    Returns:
        None
    '''

    plt.figure()
    plot_bgr(img)
    plt.title('Green: ({}, {})  Red: ({}, {})'.format(roll_g[0],
              roll_g[1], roll_r[0], roll_r[1]))
    plt.xticks([]), plt.yticks([])

    return


def plot_bgr(img):
    '''
    Plots an image in BGR colorspace in RGB which is the default in Matplotlib

    Args:
        img: array - image in BGR colorspace

    Returns:
        None
    '''

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    return


def plot_fig(img, img_title='Image'):
    '''
    Plot single image in BGR colorspace

    Args:
        img: array - image to be plotted

    Returns:
        None
    '''

    plt.figure()
    plot_bgr(img)
    plt.title(img_title)
    plt.xticks([]), plt.yticks([])

    return


def plot_1x2(img1, img2, img1_title='', img2_title=''):
    '''
    Plots two image in BGR colorspace in an 1x2 array

    Args:
        img1, img2: arrays - images to be plotted

    Returns:
        None
    '''

    plt.figure()
    plt.subplot(121), plot_bgr(img1), plt.title(img1_title)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plot_bgr(img2), plt.title(img2_title)
    plt.xticks([]), plt.yticks([])

    return
