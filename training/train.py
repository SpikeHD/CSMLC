from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8n.pt')
model.to('cuda')

if __name__ == '__main__':
   # Use the model
   results = model.train(
      data='S:/CSMLC/training/custom.yaml',
      imgsz=800,
      epochs=20,
      batch=8,
      name='yolov8n_custom'
   )