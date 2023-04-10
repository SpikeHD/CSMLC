from ultralytics import YOLO
import time
import cv2
import numpy as np
import dxcam
from ultralytics.yolo.utils.plotting import Annotator

import trigger

# load best.pt
model = YOLO('./training/best.pt')
model.to('cuda')

camera = dxcam.create()
frame = camera.grab()  # full screen

last_tb = time.time()

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

      annotator = Annotator(frame)
      boxes = result.boxes

      for box in boxes:
        b = box.xyxy[0]  # get box coordinates in (top, left, bottom, right) format
        c = box.cls
        annotator.box_label(b, model.names[int(c)])

        if closest_box is None or b[1] < closest_box[1]:
          closest_box = b
    
    if closest_box is not None:
      box_arr = np.array(closest_box.cpu(), dtype=np.int32)

      if time.time() - last_tb > 1:
        
        # do triggerbot from trigger.py
        if trigger.trigger_check(box_arr):
          last_tb = time.time()
    
    # Downscale to 1/4
    if type(frame) is np.ndarray:
      frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

      # show the screen
      cv2.imshow('Screenshot', np.array(frame))
    
    # wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break