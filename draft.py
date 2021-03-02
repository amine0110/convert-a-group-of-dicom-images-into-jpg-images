import os
import numpy as np
import pydicom
from PIL import Image


def get_names_of_imgs_inside_folder(directory):

    names = []

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in [".dcm"]:
                names.append(filename)

    return names

def convert(directory):
    im = pydicom.dcmread('Database/'+directory)
    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)
    return final_image

names = get_names_of_imgs_inside_folder('Database')

for name in names:
    image = convert(name)
    image.save(name+'.jpg')

    