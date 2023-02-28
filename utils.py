import cv2
import numpy as np
from skimage.filters import unsharp_mask
from skimage.io import imread, imsave  # reads in image as numpy array

def bytes_to_array(image_bytes):
    image_buffer = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_buffer, cv2.IMREAD_COLOR)
    image = image[..., [2, 1, 0]]
    return image


def sharpen(image, radius, amount) -> np.ndarray:
    return unsharp_mask(image, radius=radius, amount=amount, channel_axis=2)


def save_image(filename, im):
    imsave(filename, im)