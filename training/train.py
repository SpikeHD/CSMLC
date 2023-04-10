from ultralytics import YOLO
import time
import os

# Count the images in test, train, and val folders
test_images = len(os.listdir('S:/CSMLC/training/test/images'))
train_images = len(os.listdir('S:/CSMLC/training/train/images'))
val_images = len(os.listdir('S:/CSMLC/training/val/images'))

# Load the model.
model = YOLO('yolov8n.pt')
model.to('cuda')


if __name__ == '__main__':
   start = time.time()
   
   # Use the model
   results = model.train(
      data='S:/CSMLC/training/custom.yaml',
      imgsz=928,
      epochs=30,
      batch=8,
      name='yolov8n_custom'
   )

   end = time.time()

   # Print the number of images in each folder
   print(f'{test_images} images in the test folder.')
   print(f'{train_images} images in the train folder.')
   print(f'{val_images} images in the val folder.')

   print(f'Training took {end - start} seconds (or {round((end - start) / 60, 2)} minutes)')