
def img_specs(img):
    """
    This function returns the basic description of the input image.
    :param img: input is one .jpg image
    :return: tuple of Minimum pixel value, Maximum pixel value, Image Height, Image Width, Number of channels
    """
    px_min = img.min()
    px_max = img.max()

    if len(img.shape) < 3:
        height, width = img.shape
        channels = 1
    else:
        height, width, channels = img.shape
    return px_min, px_max, height, width, channels

