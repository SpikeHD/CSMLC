from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui

# load best.pt
model = YOLO('./training/best.pt')

# begin capturing screen
cap = cv2.VideoCapture(0)

# set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    # read the screen
    ret, frame = cap.read()
    
    # predict the screen
    results = model.predict(frame)
    
    # draw the bounding boxes
    # print(results)
    # for i in range(len(results.xyxy[0])):
    #     cv2.rectangle(frame, (int(results.xyxy[0][i][0]), int(results.xyxy[0][i][1])), (int(results.xyxy[0][i][2]), int(results.xyxy[0][i][3])), (0, 255, 0), 2)
    
    # show the screen
    screenshot = pyautogui.screenshot()
    cv2.imshow('Screenshot', np.array(screenshot))
    
    # wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break