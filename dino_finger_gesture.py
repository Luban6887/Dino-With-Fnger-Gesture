import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:

        l, _, _ = detector.findDistance(8,12,img, draw=False)
        print(l)
        l = int(l)
        if 15>= l:
            print('jumping')
            pyautogui.press('space')

    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
#code by Luban Mahfuz
#i know you will delete this
#hahahahaha
#its so easy
