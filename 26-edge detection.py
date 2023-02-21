# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:55:19 2023

@author: harsha
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("D:/git/image_repo/lioness.jpg")

#build a kernel and convolve
kernel = np.ones((5,5),dtype=np.float32)/25
#-1 will give the output image smae as the input image
filt = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(3,3))
gauss_blut = cv.GaussianBlur(img,(5,5),0)
medain = cv.medianBlur(img,3)
biltaeral = cv.bilateralFilter(img,9,75,75)
plt.imshow(biltaeral)