from ultralytics import YOLO
import cv2
import numpy as np
import dxcam
from ultralytics.yolo.utils.plotting import Annotator

# load best.pt
model = YOLO('./training/best.pt')
model.to('cuda')

camera = dxcam.create()
frame = camera.grab()  # full screen

while True:
    # read the screen
    frame = camera.grab()

    if type(frame) is np.ndarray:
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # predict the screen
    results = model.predict(frame, conf=0.25)
    
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
    
    # Downscale to 1/4
    if type(frame) is np.ndarray:
      frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

      # show the screen
      cv2.imshow('Screenshot', np.array(frame))
    
    # wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break