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
        img_1 = img.copy()
        img_1[:, :] = cv2.equalizeHist(img_1[:, :])

        img_1 = cv2.resize(img_1, (img_width, img_height), interpolation=cv2.INTER_CUBIC)
        plt.imshow(img_1[:, :])
        plt.title("after histogram equalization")
        plt.tight_layout()
        plt.show(block=False)
    else:
        plt.imshow(img[:, :, ::-1])
        plt.title("before histogram equalization")
        plt.show(block=False)

        img_height = img_info.img_specs(img)[2]
        img_width = img_info.img_specs(img)[3]
        img_1 = img.copy()
        img_1[:, :, 0] = cv2.equalizeHist(img_1[:, :, 0])
        img_1[:, :, 1] = cv2.equalizeHist(img_1[:, :, 1])
        img_1[:, :, 2] = cv2.equalizeHist(img_1[:, :, 2])

        img_1 = cv2.resize(img_1, (img_width, img_height), interpolation=cv2.INTER_CUBIC)
        plt.imshow(img_1[:, :, :])
        plt.title("after histogram equalization")
        plt.tight_layout()
        plt.show(block=False)
    return None

if __name__ == "__main__":
    equalize()
