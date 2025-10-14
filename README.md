# opencv-first-project
This Python program detects and counts apples in an image using OpenCV. It is my first computer vision project and demonstrates basic image processing, color detection, and circle detection techniques.

Features

Loads an image of an apple tree (apple_tree.jpg).

Converts the image from BGR to HSV color space for better color detection.

Detects red apples using defined color thresholds.

Reduces noise using Gaussian blur.

Detects circular shapes (apples) using Hough Circle Transform.

Draws green circles around detected apples and red dots at their centers.

Prints the total number of apples found in the image.

Requirements

Python 3.x

OpenCV (cv2)

NumPy (numpy)

Install the required packages using pip:

pip install opencv-python numpy

Usage

Place an image of an apple tree in the same folder as the script and name it apple_tree.jpg.

Run the script:

python apple_counter.py


The program will:

Display the image with detected apples circled.

Print the total number of apples in the console. For the provided image, the output is:

Number of apples: 9

How It Works

The image is converted to HSV color space for easier color segmentation.

Two red color ranges are defined to capture different shades of red.

A mask is created to isolate red regions (potential apples).

Gaussian blur is applied to reduce noise and improve circle detection.

Hough Circle Transform detects circles in the mask corresponding to apples.

Detected apples are drawn on the image, and the total count is calculated.

Notes

HSV color space is more robust than RGB for color-based detection.

Hough Circle Transform is suitable for detecting round objects like apples.

This project marks my first hands-on experience in computer vision and helped me understand how to process images and detect objects with OpenCV.
