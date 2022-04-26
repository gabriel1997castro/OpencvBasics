import cv2
import numpy as np

img = cv2.imread("resources/test.png")
print(img.shape)

imgResize = cv2.resize(img, (300,200))
imgCropped = imgResize[0:100, 150:300]

cv2.imshow("Image resized", imgResize)
cv2.imshow("Image cropped", imgCropped)

cv2.waitKey(0)
