import cv2
import matplotlib.pyplot as plt
from Bipp import info

class Bipp():

    def __init__(self):
        return

    def plothist(img):
        """
        This function plots the histogram of image pixel values across channels
        :param img: input is one .jpg image
        :return: a histogram of image pixel values across channels
        """

        if len(img.shape)<3:
            max = info.img_specs(img)[1]
            min = info.img_specs(img)[0]    
            hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[int(max)], ranges=[int(min), int(max)])
            plt.plot(hist)
            plt.xlim(int(min), int(max))
            plt.title('Histogram for grey image')
            plt.xlabel("Bins")
            plt.ylabel("# of Pixels")
            plt.show(block=True)
        else:
            color = ('b', 'g', 'r')
            for channel, col in enumerate(color):
                hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[int(max)], ranges=[int(min), int(max)])
                plt.plot(hist, color=col, label=col)
                plt.legend()
                plt.xlim(int(min), int(max))
            plt.title('Histogram for colored image')
            plt.xlabel("Bins")
            plt.ylabel("# of Pixels")
            plt.show(block=True)
        return None

    def equalize(img):
        """
        This function improves the contrast of input image
        :param img: input is one .jpg image
        :return: image comparison before & after histogram equalization
        """
        if len(img.shape)<3:
            plt.imshow(img[:, :])
            plt.title("before histogram equalization")
            plt.show(block=False)

            img_height = info.img_specs(img)[2]
            img_width = info.img_specs(img)[3]
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

            img_height = info.img_specs(img)[2]
            img_width = info.img_specs(img)[3]
            img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
            img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
            img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

            img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_CUBIC)
            plt.imshow(img[:, :, :])
            plt.title("after histogram equalization")
            plt.tight_layout()
            plt.show(block=False)
        return img

    def imgresize(img):
        """
        This function resizes the images
        :param img: input is one .jpg image
        :return: Resized image height and width
        """
        if info.img_specs(img)[2] > 300:
            img_height = 300
        else:
            img_height = info.img_specs(img)[2]

        if info.img_specs(img)[3] > 500:
            img_width = 500
        else:
            img_width = info.img_specs(img)[3]

        return img_height, img_width

    def imgsplit(img):
        """
        splitting images by channels
        :param img: input is one .jpg image
        :return: image in 3 different channels
        """
        if len(img.shape)==3:
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

            img_height = Bipp.imgresize(img)[0]
            img_width = Bipp.imgresize(img)[1]

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

if __name__ == "__main__":
    Bipp()
