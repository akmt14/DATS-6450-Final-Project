#Author: Purvi Thakor, Akshay Kamath
import cv2
import matplotlib.pyplot as plt
from Bipp import img_info

class plots():

    def __init__(self):
        return

    def pxl_histogram(img):
        """
        This function plots the histogram of image pixel values across channels
        :param img: input is one .jpg image
        :return: a histogram of image pixel values across channels
        """
        max = img_info.img_specs(img)[1]
        min = img_info.img_specs(img)[0]

        if len(img.shape)<3:
            hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[int(max)], ranges=[int(max), int(min)])
            plt.plot(hist)
            plt.xlim(int(min), int(max))
            plt.title('Histogram for grey image')
            plt.xlabel("Bins")
            plt.ylabel("No. of Pixels")
            plt.show(block=True)
        else:
            color = ('b', 'g', 'r')
            for channel, col in enumerate(color):
                hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[int(max)], ranges=[int(max), int(min)])
                plt.plot(hist, color=col, label=col)
                plt.legend()
                plt.xlim(int(min), int(max))
            plt.title('Histogram for colored image')
            plt.xlabel("Bins")
            plt.ylabel("No. of Pixels")
            plt.show(block=True)
        return None

if __name__ == "__main__":
    plots()
