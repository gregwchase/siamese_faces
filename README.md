# Siamese Faces
## Applied Facial Recognition with Siamese Neural Networks

## Overview
Facial recognition is a common task performed in a variety of industries. Companies like Facebook use this tool for
identifying faces in uploaded user photos, while Baidu uses this for employee facial recognition.

This task seeks to check contrastive loss between similar images of people.


## Table of Contents
1. [Data Set](#data set)
2. [Preprocessing](#preprocessing)
3. [Model](#model)
4. [Results](#results)
5. [Tech Stack](#tech-stack)
6. [References](#references)


## Data Set
The data consists of 25 head shots from the Galvanize g49 Data Science Immersive cohort.


## Preprocessing
All images were converted from RGB to grayscale. Using OpenCV, the faces within each image are cropped, and saved to a
new directory. The images are then resized to 512 x 512.

Finally, all images were mirrored using OpenCV. This is to look at contrastive loss between two photos of the same person.


## Model


## Results


## Tech Stack

* OpenCV


## References
* [Siamese Networks With PyTorch](https://hackernoon.com/facial-similarity-with-siamese-networks-in-pytorch-9642aa9db2f7)
* [Face Detection on Your Photo Collection in Python](https://simplyml.com/face-detection-on-your-photo-collection-in-python/)
* [Face Detection Using OpenCV and Python: A Beginner’s Guide](https://www.superdatascience.com/opencv-face-detection/)
