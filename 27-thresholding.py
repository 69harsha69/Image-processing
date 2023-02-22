# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:53:14 2023

@author: harsha
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import skimage.exposure as exp
from skimage.restoration import denoise_nl_means,estimate_sigma
from skimage import io,img_as_float,img_as_ubyte

img = (io.imread("D:/git/image_repo/Alloy_noisy.jpg"))
img = nd.median_filter(img,size=3)

eq_img = cv.equalizeHist(img)

#contrast lmimited adaptive histogrma equalization
clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize = (8,8))
cl_img = clahe.apply(img)

# plt.hist(cl_img.flat,bins = 100 ,range =(90,255))


r,thresh1 = cv.threshold(cl_img,190,150,cv.THRESH_BINARY) #until what values you threshold and value replaced 
r,thresh = cv.threshold(cl_img,190,255,cv.THRESH_BINARY_INV)
r,thresh2 = cv.threshold(cl_img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

kernel = np.ones((3,3),dtype=np.uint8)
erosion = cv.erode(thresh2,kernel,iterations=1)
dilation = cv.dilate(thresh2,kernel,iterations=1)
opening =cv.morphologyEx(thresh2,cv.MORPH_CLOSE,kernel)
closing =cv.morphologyEx(thresh2,cv.MORPH_OPEN,kernel)
plt.imshow(closing)