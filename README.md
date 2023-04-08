<div align="center">
  <h1>CSMLC</h1
  <p>
    <b>C</b>ounter <b>S</b>trike <b>M</b>achine <b>L</b>earning <b>C</b>heats is a project I created to learn image recognition machine learning. Using a modified <a href="https://github.com/SpikeHD/cs2-data-dumper">CS2 ESP program</a> to dump bounding box data into YOLO format, I am able to efficiently gather training data after just a little bit of cleanup!
  </p>
</div>

# Table of contents
- [Progress](#progress)
- [Setup](#setup)
  - [For training](#for-training)
  - [For using](#for-using)

# Progress

Here is an example video of the current model (as of April 7, 2023)!

<div align="center">
  <video src="https://user-images.githubusercontent.com/25207995/230737594-096aabe8-e91f-4739-9771-54b227ed62fc.mp4" />
</div>

# Setup

Both training and usage require the installation of [Python 3](https://www.python.org/). Trust me, I *also* wish this were not the case. C++ compiled binaries one day I promise.

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
