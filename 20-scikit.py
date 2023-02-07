# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:57:05 2023

@author: harsha
"""

from skimage import io
import matplotlib.pyplot as plt
from skimage import transform,filters,feature
from skimage import restoration
import scipy.stats as st
import numpy as np

img  = io.imread("D:/git/image_repo/lioness.jpg", as_gray =True)

rescaled = transform.rescale(img, 1.0/4.0,anti_aliasing=True)
resied = transform.resize(img, (200,200))
downscale = transform.downscale_local_mean(img, (2,1))

#filters edge detection
edge_roberts = filters.roberts(img)
edge_sobel = filters.sobel(img)
edge_scharr = filters.scharr(img)
edge_prewitt = filters.prewitt(img)
#in canny the sigma controls the edge detection
#noise reduciton,gradient calculation also edge tracking
edge_canny = feature.canny(img,sigma = 1)

#deconvolving 
psf = np.ones((3,3))/9 #average point spread function
#creating a gaussian psf
def gkern(klen,nsig):
    lim = klen//2 + (klen%2)/2
    x = np.linspace(-lim, lim,klen+1)
    ker1d = np.diff(st.norm.cdf(x))
    ker2d = np.outer(ker1d, ker1d)
    return ker2d/ker2d.sum()

psf = gkern(5,3)
deconvolved,_ = restoration.unsupervised_wiener(img, psf)

plt.subplot(121)
plt.imshow(img,cmap = plt.cm.gray)
plt.subplot(122)
plt.imshow(deconvolved,cmap = plt.cm.gray)   
plt.tight_layout()

# ########
# #plotting
# fig,axes = plt.subplots(nrows = 2, ncols = 3,sharex=True,sharey =True,figsize=(12,8))
# ax = axes.ravel()
# ax[0].imshow(edge_roberts,cmap = plt.cm.gray)
# ax[0].set_title("edge_roberts")
# ax[1].imshow(edge_prewitt,cmap = plt.cm.gray)
# ax[1].set_title("edge_prewitt")
# ax[2].imshow(edge_scharr,cmap = plt.cm.gray)
# ax[2].set_title("edge_scharr")
# ax[3].imshow(edge_sobel,cmap = plt.cm.gray)
# ax[3].set_title("edge_sobel")
# ax[4].imshow(edge_canny,cmap = plt.cm.gray)
# ax[4].set_title("edge_canny")
# ax[5].imshow(deconvolved,cmap = plt.cm.gray)
# ax[5].set_title("deconvolved")
# for a in ax:
#     a.axis('off')
# plt.tight_layout()
# ########