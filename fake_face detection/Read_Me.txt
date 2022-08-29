Steps to Run the code on linux:
Required libraries to run on the command line.
pip install pandas
pip install numpy
pip install matplotlib
pip install pillow
pip install torchaudio
Changes made in the code in train.py file 
import os 


Data segmentation:
link for data: https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection

The data was into comprised 3 folders: test, train, validate

Inside the train, test and validate folders there should be folders bearing a specific number which corresponds to a specific category

For example, if we have the image x.jpg and it is a lotus it could be in a path like this /test/real/x.jpg



Instruction to Run the model.
Train a new network on a data set with train.py

Basic Usage : python train.py data_directory(path of data)
Output: A trained network ready with checkpoint and a .onnx file of the model saved for parsing of face images and identifying the "realness" of the face.
Predict an image class with predict.py along with the probability. That is you'll pass in a single image /path/to/image

Basic usage: python predict.py /path/to/image
Output: The probability a face is real or fake
