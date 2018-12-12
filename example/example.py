import cv2
from Bipp import ImgProc, img_info, img_equalization, img_splitting

img = cv2.imread("../test_images/colored1.jpg")

#returns image specifications
img_info.img_specs(img)

#is a class that returns histogram of pixels across channels
ImgProc.plots.pxl_histogram(img)

#returns images with improved contrast
img_equalization.equalize(img)

#returns input image split into 3 channels
img_splitting.imgsplit(img)

