# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:49:20 2023

@author: harsha
"""

from skimage.restoration import denoise_nl_means,estimate_sigma
from skimage import img_as_float,img_as_ubyte,io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as nd

img = img_as_float(io.imread("D:/git/image_repo/segment_noisy.jpg",as_gray = True))
sigma_est = np.mean(estimate_sigma(img,multichannel=False))
denoise = denoise_nl_means(img,h = 1.15*sigma_est,fast_mode=True,patch_size = 5,patch_distance=5,multichannel=False)

denoise_8bit = img_as_ubyte(denoise)

# plt.hist(denoise_8bit.flat,bins = 100,range=(0,255))
seg1 = denoise_8bit <= 55
seg2 = (denoise_8bit > 55) & (denoise_8bit <= 110)
seg3 = (denoise_8bit > 120) & (denoise_8bit <= 210)
seg4 = (denoise_8bit > 210)




seg1_closed = nd.binary_closing(seg1,np.ones((3,3)))
seg1_opened = nd.binary_opening(seg1_closed,np.ones((3,3)))

seg2_closed = nd.binary_closing(seg2,np.ones((3,3)))
seg2_opened = nd.binary_opening(seg2_closed,np.ones((3,3)))

seg3_closed = nd.binary_closing(seg3,np.ones((3,3)))
seg3_opened = nd.binary_opening(seg3_closed,np.ones((3,3)))

seg4_closed = nd.binary_closing(seg4,np.ones((3,3)))
seg4_opened = nd.binary_opening(seg4_closed,np.ones((3,3)))

all_segments = np.zeros((denoise_8bit.shape[0],denoise_8bit.shape[1],3))
all_segments[seg1_opened] = (1,0,0)
all_segments[seg2_closed] = (0,1,0)
all_segments[seg3_closed] = (0,0,1)
all_segments[seg4_closed] = (1,1,0)
plt.imshow(all_segments)