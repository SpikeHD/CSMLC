from ultralytics import YOLO
import time
import cv2
import numpy as np
import dxcam
from ultralytics.yolo.utils.plotting import Annotator
from pynput import mouse

import trigger
import aim

# load best.pt
model = YOLO('training/best.pt')
model.to('cuda')

camera = dxcam.create()
frame = camera.grab()  # full screen

last_tb = time.time()
last_aim = time.time()

left_clicking = False

def on_click(x, y, button, pressed):
  global left_clicking
  if button == mouse.Button.left:
    left_clicking = pressed


listener = mouse.Listener(on_click=on_click)
listener.start()

while True:
  # read the screen
  frame = camera.grab()

  if type(frame) is np.ndarray:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  # predict the screen
  results = model.predict(frame, conf=0.25, verbose=False)
  closest_box = None
      
  # draw the bounding boxes
  for result in results:
    if hasattr(result.boxes, 'xyxy') and len(result.boxes.xyxy) <= 0:
      continue
        
    try:
      annotator = Annotator(np.ascontiguousarray(frame))
      boxes = result.boxes

      for box in boxes:
        b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
        c = box.cls
        annotator.box_label(b, model.names[int(c)])

        if closest_box is None or b[1] < closest_box[1]:
          closest_box = b
    except:
      pass
      
  # If there is a close box, check to see if we can do stuff with it
  if closest_box is not None:
    box_arr = np.array(closest_box.cpu(), dtype=np.int32)

    # if time.time() - last_tb > 0.1:
    #   # do triggerbot from trigger.py
    #   if trigger.trigger_check(box_arr):
    #     last_tb = time.time()

    if time.time() - last_aim > 0.2 and left_clicking:
      if aim.aim_check(box_arr, listener):
        last_aim = time.time()
      
  # Downscale to 1/4
  if type(frame) is np.ndarray:
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)
    # show the screen
    cv2.imshow('Screenshot', np.array(frame))
      
  # wait for a key press
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
      