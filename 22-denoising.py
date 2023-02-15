# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:36:59 2023

@author: harsha
"""

#improve quality of images --> denoise the image
#difital filters are convolution b/w a  kernel and image
#kernel is a matrial 
#can be linear and non linear

import numpy as np
from skimage import io,img_as_float
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.ndimage as nd
from skimage.restoration import denoise_nl_means,estimate_sigma

def gkern(klen,nsig):
    x = np.linspace(-(klen-1)/2, (klen-1)/2,klen)
    ker1d = np.exp(-0.5*np.square(x)/np.square(nsig))
    ker2d = np.outer(ker1d, ker1d)
    return ker2d/ker2d.sum()

#denoising using gaussian
img  = io.imread("D:/git/image_repo/lioness.jpg", as_gray =True)
gauss_img = nd.gaussian_filter(img,5)
gauss_kernel = gkern(9, 5) 
gauss_blur = nd.convolve(img,gauss_kernel)

#denoising using median filter
median_img = nd.median_filter(img,size=3)


#denoising by non local means
sigma = np.mean(estimate_sigma(img,multichannel=False))
nlm = denoise_nl_means(img,h=1.15*sigma,fast_mode=True,patch_size = 5,patch_distance=3,multichannel=False)


# plt.subplot(1,4,1)
# plt.imshow(gauss_img)
# plt.subplot(1,4,2)
# plt.imshow(gauss_blur)
# plt.subplot(1,4,3)
# plt.imshow(median_img)
# plt.subplot(1,4,4)
# plt.imshow(img_as_float(nlm))
# plt.tight_layout()