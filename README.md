# DATS-6450-Final-Project
Basic Image Processing Package

This is a visualization package based on opencv.

Basic functionalities -   

- gives the shape of an image (max pixel value, min pixel value, width, height, channels)
- plots a histogram of the image's pixel values
- equalizes the input images (improves image contrast)
- splits colored image into 3 channels (R,B,G)

Installation

'''
git clone https://github.com/akmt14/DATS-6450-Final-Project.git
'''

Example

'''
import cv2
from Bipp import ImgProc, img_info, img_equalization, img_splitting

img = cv2.imread("../test_images/colored1.jpg")

