# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:13:34 2023

@author: harsha
"""

from skimage import io
import matplotlib.pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.filters import try_all_threshold,threshold_otsu
import numpy as np


img  = io.imread("D:/git/image_repo/lioness.jpg", as_gray =True)
entropy_img = entropy(img, disk(3))
plt.imshow(entropy_img, cmap = plt.cm.gray)

#check which threshold works best
# fig,ax = try_all_threshold(entropy_img,verbose = False)


thresh = threshold_otsu(entropy_img)
binary = entropy_img <= thresh
