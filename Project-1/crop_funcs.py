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

    t, l = find_top_left(img, black_threshold, counter_threshold)
    b, r = find_bottom_right(img, black_threshold, counter_threshold)

    # in case boundaries are not detected in a reasonable range, do not
    # crop anything
    t_lim, b_lim = 0.1 * h, 0.9 * h
    l_lim, r_lim = 0.1 * w, 0.9 * w

    t = 0 if t > t_lim else t
    b = h if b < b_lim else b
    l = 0 if l > l_lim else l
    r = w if r < r_lim else r

    return t, b, l, r


def find_top_left(img, black_threshold, counter_threshold):
    '''
    Finds top left corner of the border

    Args:
        img: array - image with the border
        black_threshold: int - black cutoff value
        counter_threshold: int - number of continuous pixels to be checked
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
