import cv2

img = cv2.imread('1.png')
image = cv2.imread('1.png')
print(img.shape)

for i in range(0,938):
    for j in range(0,40):
        image[j,i] = [+1,+1,+1]

cv2.imshow('Before', img)
cv2.imshow('After', image)
cv2.waitKey(0)

cv2.destoryAllWindows(0)
        
