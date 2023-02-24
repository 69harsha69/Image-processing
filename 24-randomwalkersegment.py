# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:21:44 2023

@author: harsha
"""

from skimage import io,img_as_float
from skimage.restoration import estimate_sigma,denoise_nl_means
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np
from skimage.segmentation import random_walker

img = img_as_float(io.imread("D:/git/image_repo/Alloy_noisy.jpg"))

#denoise using nlmeans
sigma_est = np.mean(estimate_sigma(img,multichannel=False))
denoise = denoise_nl_means(img,h = 1.15*sigma_est,fast_mode=True,patch_size = 5,patch_distance=6,multichannel=False)

#do histogram equalizaiton
#Stretching the histogram
eq_hist = exposure.equalize_adapthist(denoise)

#random walker
markers = np.zeros(img.shape,dtype=np.uint)
markers[(eq_hist < 0.6) & (eq_hist > 0.3)] = 1
markers[(eq_hist < 0.99) & (eq_hist > 0.8)] = 2

labels = random_walker(eq_hist, markers,beta=10,mode='bf')
plt.imshow(labels,cmap = plt.cm.gray)
# plt.hist(eq_hist.flat,bins = 100,range=(0,1))
