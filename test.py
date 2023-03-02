import cv2
import time
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    print(img.shape)
    time.sleep(0.1)