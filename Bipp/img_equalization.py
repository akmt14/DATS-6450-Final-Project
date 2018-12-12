import cv2
import matplotlib.pyplot as plt
from Bipp import img_info

def equalize(img):
    """
    This function improves the contrast of input image
    :param img: input is one .jpg image
    :return: image comparison before & after histogram equalization
    """
    if len(img.shape) < 3:
        plt.imshow(img[:, :])
        plt.title("before histogram equalization")
        plt.show(block=False)

        img_height = img_info.img_specs(img)[2]
        img_width = img_info.img_specs(img)[3]
        img[:, :] = cv2.equalizeHist(img[:, :])

        img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_CUBIC)
        plt.imshow(img[:, :])
        plt.title("after histogram equalization")
        plt.tight_layout()
        plt.show(block=False)
    else:
        plt.imshow(img[:, :, ::-1])
        plt.title("before histogram equalization")
        plt.show(block=False)

        img_height = img_info.img_specs(img)[2]
        img_width = img_info.img_specs(img)[3]
        img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
        img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
        img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

        img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_CUBIC)
        plt.imshow(img[:, :, :])
        plt.title("after histogram equalization")
        plt.tight_layout()
        plt.show(block=False)
    return img
