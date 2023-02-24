# Threshold

It is the simplest method of segmenting images.From a grayscale to a binary image in general.

## simple threshold

* **BINARY** - this is straight forward.Any value below T is set to 0 else 1

* **BINARY INVERSE** - same as above but Any value below T is set to 1 else 0

* **Truncate** - The destination pixel is set to threshold T if s(x,y)(pixel value) is greater than T else left alone

* **ToZERO** - Here the destination pixel is set to zero if less than T and rest are left alone

* **ToZERO INVERSE** - same as above but is set to zero if >T

## Adaptive threshold

* **Isodata** - kind of thresholding which automatically finds a threshold for a given grayvalue image.consider a
threshold t in range of grayvlues.then\
  ml = mean of pixles s(x,y) < t so its a funciton of t\
  mh = mean of pixles s(x,y) > t so its also a funciton of t\
  t = ml+mh/2
 
![isodata](https://user-images.githubusercontent.com/123463350/217581718-2c2b5938-6506-489c-8bff-c6f0e458c00a.PNG)\

* **Yen** - 

* **OTSU** -  Usually otsu thresholding is done when there are 2 peaks in histogram.The threshold value is which minimizes the class variances(bg and fg)



* **Triangle** - line is drawn from highest bar in histogram to the end of the histogram.The largest perpendicular histance from the line to each bar under this line is considered as optimal threshold


![triangle](https://user-images.githubusercontent.com/123463350/221206287-77a3a9a2-0563-4fe6-ba89-e4575018c8c2.PNG)



