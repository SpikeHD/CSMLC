from ultralytics import YOLO

# Load the model.
model = YOLO('../training/best.pt')
model.to('cuda')

if __name__ == '__main__':
   # Pick a random image from test/images/
   results = model.predict('training/test/images/00280.png', save=True)
        