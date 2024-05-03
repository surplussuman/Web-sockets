import cv2

img = cv2.imread("suman.jpg")
img1 = cv2.resize(img, (600,600))
cv2.imshow("Image",img)
cv2.waitKey(0) 