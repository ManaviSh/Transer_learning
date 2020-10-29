# Transfer Learning using PyTorch via ResNet-18 model
Transfer learning (TL) is a research problem in machine learning (ML) that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem. Here we use a pretrained ResNet-18 model to train self organized dataset of cats, dogs and pandas to get a good accuracy. This is implemented using Pytorch. PyTorch is an open source machine learning library for Python and is completely based on Torch. The major features of PyTorch is that it has easy interface, very simple to operate and runs on Python. The code execution in this framework is quite easy. PyTorch provides an excellent platform which offers dynamic computational graphs. Thus a user can change them during runtime. <br />
The model I used is ResNet. Residual Networks learn residual functions with reference to the layer inputs, instead of learning unreferenced functions. Instead of hoping each few stacked layers directly fit a desired underlying mapping, residual nets let these layers fit a residual mapping. They stack residual blocks ontop of each other to form network. A ResNet-18 has 18 layers using these blocks. The 1st, 2nd and 3rd layers are skipped to avoid the problem of vanishing gradient. Stochastic gradient descent optimizer is used which helps in reducing the computational burden, achieving faster iterations in trade for a lower convergence rate. At the end a fully connected classfication layer is added to define labels and features of my dataset.
## Installation
- opencv
- torchvision
- numpy
- time
(note: this is without CUDA version)
## Problem Statement
Deep Learning is awesome, it has given wings to computer vision and object detection/classification. However you need a lot of data to train a good detection model which may not be readily available. Show use the use of transfer learning to train a model on less data (<1000 images) and still getting good results (>80% accuracy) to demonstrate use of transfer learning. You are free to pick a model of your choice and dataset of your choice.
## Deliverables
a. Source code of your python script (either in email or link to your github repo)
b. List of websites/articles which you found helpful while doing your search
c. A small writeup
## Result
dataset size = 1000 per label<br />
Validation Accuracy = 89.5

## Credits
Convolutional Neural Network course by Andrew Ng <br />
https://blog.paperspace.com/popular-deep-learning-architectures-resnet-inceptionv3-squeezenet/ <br />
https://app.pluralsight.com/guides/introduction-to-resnet 
