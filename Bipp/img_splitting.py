import cv2
from Bipp import img_info

def imgresize(img):
    """
    This function resizes the images
    :param img: input is one .jpg image
    :return: Resized image height and width
    """
    if img_info.img_specs(img)[2] > 300:
        img_height = 300
    else:
        img_height = img_info.img_specs(img)[2]

    if img_info.img_specs(img)[3] > 500:
        img_width = 500
    else:
        img_width = img_info.img_specs(img)[3]

    return img_height, img_width


def imgsplit(img):
    """
    splitting images by channels
    :param img: input is one .jpg image
    :return: image in 3 different channels
    """
    if len(img.shape) == 3:
        b = img.copy()
        # set green and red channels to 0
        b[:, :, 1] = 0
        b[:, :, 2] = 0

        g = img.copy()
        # set blue and red channels to 0
        g[:, :, 0] = 0
        g[:, :, 2] = 0

        r = img.copy()
        # set blue and green channels to 0
        r[:, :, 0] = 0
        r[:, :, 1] = 0

        img_height = imgresize(img)[0]
        img_width = imgresize(img)[1]

        imsize_b = cv2.resize(b, (img_width, img_height))
        imsize_g = cv2.resize(g, (img_width, img_height))
        imsize_r = cv2.resize(r, (img_width, img_height))

        cv2.imshow("blue channel", imsize_b)
        cv2.waitKey(0)

        cv2.imshow("green channel", imsize_g)
        cv2.waitKey(0)

        cv2.imshow("red channel", imsize_r)
        cv2.waitKey(0)
    else:
        print("Grayscale image can't be splitted")

        return

