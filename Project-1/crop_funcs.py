def crop_aligned_image(img, roll_g, roll_r):
    '''
    Crop the aligned image consideing the outside border and the amount of
    pixels the G and R layers were rolled to align them.

    Args:
        img: array - aligned image
        roll_g: tuple - amount of pixels the G layer was rolled to align it
                with B layer
        roll_r: tuple - amount of pixels the R layer was rolled to align it
                with B layer

    Returns:
        cropped: array - cropped image
    '''
    
    h, w, c = img.shape

    crop_outer = 0.04
    t, b, l, r = crop_limits(h, w, crop_outer)
    t_adj, b_adj = crop_limits_gr(roll_g[0], roll_r[0])
    l_adj, r_adj = crop_limits_gr(roll_g[1], roll_r[1])

    cropped = img[t + t_adj:b + b_adj, l + l_adj:r + r_adj, :]

    return cropped


def crop_limits_gr(g, r):
    '''
    Finds the crop limits based on the pixels of G and R layer were rolled in
    order to align them with B layer.

    Args:
        g: int - number of pixels G layer was rolled
        r: int - number of pixels R layer was rolled

    Returns:
        crop1, crop2: ints - amount of pixels to be cropped on top/left side
                      and on bottom/right side
    '''

    crop1, crop2 = 0, 0
    if g > 0 and r > 0:
        crop1 = max([g, r])
    elif g < 0 and r < 0:
        crop2 = min([g, r])
    elif g > 0 and r < 0:
        crop1, crop2 = g, r
    elif g < 0 and r > 0:
        crop1, crop2 = r, g

    return crop1, crop2


def crop_limits(h, w, p):
    '''
    Calculates crop limis in pixels so that an image can be cropped by a
    percent along all borders

    Args:
        h: int - height of the image
        w: int - width of the image
        p: double - percentage (between 0.0 - 1.0) crop limits

    Returns:
        t, b, l, r: ints - top, bottom, left, right pixel values
    '''

    crop_percent = p

    t = int(crop_percent * h)
    b = int((1 - crop_percent) * h)
    l = int(crop_percent * w)
    r = int((1 - crop_percent) * w)

    return t, b, l, r


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
    t_lim, b_lim, l_lim, r_lim = crop_limits(h, w, 0.1)

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
