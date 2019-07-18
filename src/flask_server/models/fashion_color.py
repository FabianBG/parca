import numpy as np
from PIL import Image
import itertools
from keras.applications.mobilenet import preprocess_input as mpi
from keras.preprocessing.image import img_to_array
import cv2
import imutils

labels = ["black", "blue", "dress", "jeans", "red", "shirt"]
input_size = (96, 96)

def decode_output(output):
    others = []
    for value, label in zip(output, labels):
        others.append((str(value * 100) + " %", label))
    others.sort(key=lambda x: x[0])
    return  {
        "predictions": others[::-1]
    }

def preprocess_image(path):
    image = cv2.imread(path)
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    return np.expand_dims(image, axis=0)
    

def generate_input(path, input_data):
    return {
        "signature_name": "predict",
        "inputs": np.array(input_data).tolist() 
    }