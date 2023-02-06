# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:05:50 2023

@author: harsha
"""
#first git commits
from scipy import ndimage
from skimage import io,img_as_float,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

img = img_as_ubyte(io.imread("D:\git\image_repo\oilglands.jpg",as_gray = True))
print(img.shape,img.dtype)
print(img.mean(),img.max(),img.min())

flippedLR = np.fliplr(img)
flippedUD = np.flipud(img)
rotated = ndimage.rotate(img, 75)
#smoothing or denoising techniques
uniform_filtered = ndimage.uniform_filter(img,size=9)
#gaussian preserved edges
#median is a better one whihc preserves edges
#these cmaps only work on single channekl images

median_filtered = ndimage.median_filter(img,size=3)

sobel_x = ndimage.sobel(img,axis=0)
sobel_y = ndimage.sobel(img,axis=1)
plt.subplot(1,2,1)
plt.imshow(sobel_x)
plt.subplot(1,2,2)
plt.imshow(sobel_y)
plt.show()
# plt.subplot(2,2,1) 
# plt.imshow(uniform_filtered,cmap = 'gray')
# plt.subplot(2,2,2)
# plt.imshow(rotated)
# plt.subplot(2,2,3)
# plt.imshow(flippedLR,cmap = 'Blues')
# plt.subplot(2,2,4)
# plt.imshow(flippedUD,cmap = 'hsv')