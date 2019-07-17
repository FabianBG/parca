import numpy as np
from PIL import Image
import itertools

labels = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

def decode_output(output):
    better_index = np.argmax(output)
    others = []
    for value, label in zip(output, labels):
        others.append((value, label))
    return  {
        "label": (output[better_index], labels[better_index]),
        "others": others
    }
    

def generate_input(path, input_data):
    return {
        "signature_name": "predict",
        "inputs": np.array(input_data).tolist() 
    }