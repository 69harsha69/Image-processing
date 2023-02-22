# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:03:27 2023

@author: harsha
"""

import cv2 as cv
import numpy as np
from scipy.signal import convolve2d 
import matplotlib.pyplot as plt
from skimage.util import random_noise
from scipy.ndimage import gaussian_filter

img = cv.imread("D:\git\image_repo\corner.png",0)
img  = cv.resize(img,dsize=(500,500))
# img = random_noise(img, mode='s&p',amount=0.2)
gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

#while filter2d direct convolution
x_gradient = convolve2d(img, gx_kernel,mode='same')
y_gradient = convolve2d(img, gy_kernel,mode='same')

gradient_magnitude = np.sqrt(np.square(x_gradient) + np.square(y_gradient))
gradient_magnitude *= 255/gradient_magnitude.max()


ixx = gaussian_filter(x_gradient**2, sigma=1)
ixy = gaussian_filter(y_gradient*x_gradient, sigma=1)
iyy = gaussian_filter(y_gradient**2, sigma=1)

#harris
k = 0.04
#determinent
det = ixx*iyy-ixy**2
#trace
trace = ixx+iyy
harris_response = det - k*trace**2


for row,response in enumerate(harris_response):
    for col,r in enumerate(response):
        if r>0:
            plt.scatter(col,row,c='b')
            

# offset=1
# height,width = img.shape
# for y in range(offset, height-offset):
#     for x in range(offset, width-offset):
#         Sxx = np.sum(ixx[y-offset:y+1+offset, x-offset:x+1+offset])
#         Syy = np.sum(iyy[y-offset:y+1+offset, x-offset:x+1+offset])
#         Sxy = np.sum(ixy[y-offset:y+1+offset, x-offset:x+1+offset])
        
#         #Find determinant and trace, use to get corner response
#         det = (Sxx * Syy) - (Sxy**2)
#         trace = Sxx + Syy
#         r = det - k*(trace**2)
        
        
#         if r<0:
#             plt.scatter(x,y)
            
# plt.scatter(x_gradient.ravel(),y_gradient.ravel())

m = cv.moments(img)
cx = (m["m10"] / m["m00"])
cy = (m["m01"] / m["m00"])

