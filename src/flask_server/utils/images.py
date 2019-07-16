import PIL.Image
import numpy as np

def simple_image_handler(image, model_input_size):
    x = []
    image = PIL.Image.open(image).convert('L').resize((28, 28)).resize((model_input_size))
    image = np.array(image)
    if len(image.shape) < 3: 
        image = np.stack((image,)*3, axis=-1)
    x.append(image)
    return x