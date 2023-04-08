<div align="center">

  <img height="200px" src="https://user-images.githubusercontent.com/25207995/230746716-b1cb3e91-985e-4882-97ae-88bd6fa79382.png" />

  <div>
    <img src="https://img.shields.io/github/size/SpikeHD/CSMLC/training/best.pt?label=model%20size" />
    <img src="https://img.shields.io/github/commit-activity/m/SpikeHD/CSMLC" />
    <img src="https://img.shields.io/github/last-commit/SpikeHD/CSMLC" />
   </div>
  
  <p>
    <b>C</b>ounter <b>S</b>trike <b>M</b>achine <b>L</b>earning <b>C</b>heats is a project I created to learn image recognition machine learning. Using a modified <a href="https://github.com/SpikeHD/cs2-data-dumper">CS2 ESP program</a> to dump bounding box data into YOLO format, I am able to efficiently gather training data after just a little bit of cleanup!
  </p>
  <p>Inspired by <a href="https://github.com/IgaoGuru/Sequoia">Sequoia</a> :)</p>
  
  <p><i>Disclaimer: This is created both as practice for myself and as an educational example of practical image-recognition and machine learning applications. It is not intended for use outside of private matches.</i></p>
</div>

# Table of contents
- [Progress](#progress)
- [Setup](#setup)
  - [For training](#for-training)
  - [For using](#for-using)
- [Technical Details](#technical-details)

# Progress

Here is an example video of the current model (as of April 7, 2023)! There are a couple mis-identifications, but overall I think it's really accurate.

<div align="center">
  <video src="https://user-images.githubusercontent.com/25207995/230737594-096aabe8-e91f-4739-9771-54b227ed62fc.mp4" />
</div>

# Setup

Both training and usage require the installation of [Python 3](https://www.python.org/). Trust me, I *also* wish this were not the case. C++ compiled binaries one day I promise.

This repo should always contain a `best.pt` model, which will always be updated to the best model I have trained so far. You can use this instead of training it yourself.

## For training

1. (optional) use a `venv`:
  ```sh
  python -m venv [venv name]
  .\[venv name]\Scripts\activate
  ```
2. Install `torch` with CUDA (if your GPU supports it) before installing everything else: https://pytorch.org/get-started/locally/
3. Install packages:
  ```sh
  pip install numpy ultralytics opencv-python
  ```
4. Set up folder structure:
  ```
CSMLC/
└── training/
    ├── all/
    │   ├── input/
    │   └── labels/
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── test/
    │   ├── images/
    │   └── labels/
    └── val/
        ├── images/
        └── labels/
  ```
  The `all` folder is not required, you can split your data manually if you'd like, but if you want your folder splitting automated, you can put everything in the `all` folder and run `node split.js` (requires [NodeJS](https://nodejs.org/en), will be making a python version soon probably)
  
  5. Train it!
  ```sh
  python training/train.py
  ```

**Additional notes:**
You can tweak anything training related in `custom.yaml` and `train.py`.

## For using

1. (optional) use a `venv`:
  ```sh
  python -m venv [venv name]
  .\[venv name]\Scripts\activate
  ```
2. Install `torch` with CUDA (if your GPU supports it) before installing everything else: https://pytorch.org/get-started/locally/
3. Install packages:
  ```sh
  pip install numpy ultralytics opencv-python dxcam pywin32
  ```
4. Run it!
  ```sh
  python training/screen.py
  ```
  This will run the script that opens a new window, which displays what the computer sees and shows the bounding boxes of where players are (see the [example video](#progress) for how that looks).
  
# Technical Details

This project is built off the backbone of [YOLOv8](https://github.com/ultralytics/ultralytics), a super-fast and surprisingly accurate model for machine learning applications. A lot of the projects you will see that do something similar to this one are using slightly older versions (Sequoia uses v5, for example), so this one is currently the most state-of-the-art!

To train the custom model, I gather data using a [CS2 ESP cheat](https://github.com/SpikeHD/cs2-data-dumper) that I modified (thank you to the original author of it!) to dump bounding box data directly to YOLO format. I then use my personal favorite labelling program, [OpenLabeling](https://github.com/Cartucho/OpenLabeling), to clean up the data (for example, getting rid of ESP boxes that are showing players through walls). A couple games of Deathmatch was enough to get it to it's current state.

The YOLOv8 model is awesome. In fact, I'm sure you're curious about the training time on the above [example video](#progress):

```
+-------+
| specs |
+-------+
GPU: RTX 3070 8gb
CPU: i7-9700k (not overclocked)
RAM: 32GB

+------------------+
| training metrics |
+------------------+
Images: ~1.6k (about ~17gb of uncompressed BMPs)
Epochs: 30
Resolution: 928
Batch: 8
Approx. Time Taken to Train: 1h
```
(I will try to remember to time the next training session properly)

An hour to train?? Only ~1.6k images?? I don't know what is considered "good" or "bad" in the machine learning world yet, but I'd say that's pretty impressive for the result it gives.

