# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:48:22 2023

@author: harsha
"""

import cv2 as cv

img = cv.imread("D:/git/image_repo/lioness.jpg")
#opencv color convention is BGR

b,g,r = cv.split(img)
img_merged = cv.merge((b,g,r))

#resize
img_resized = cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)

cv.imshow("output",img_resized)
cv.waitKey(0)
cv.destroyAllWindows()