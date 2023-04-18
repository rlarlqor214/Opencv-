import cv2

capture =cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()


#픽셀 하나하나를 다룰수 있도록
