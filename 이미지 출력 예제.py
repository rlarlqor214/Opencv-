import cv2 as cv

image = cv.imread("1.png")
cv.imshow("Image", image)
cv.waitkey(0)
cv.destroyAllWindows()