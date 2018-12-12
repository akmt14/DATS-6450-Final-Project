import cv2
from Bipp import ImgProc, img_info, img_equalization, img_splitting
import matplotlib.pyplot as plt

img = cv2.imread("../test_images/colored1.jpg")

ImgProc.plots.pxl_histogram(img)
img_equalization.equalize(img)
img_splitting.imgsplit(img)
imgsplit.imgsplit(img)
equalize.equalize(img)