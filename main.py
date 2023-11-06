import os
import numpy as np
import pydicom
import sys
from PIL import Image

DIR = "Database"

def get_names_of_imgs_inside_folder(directory):

    names = []

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in [".dicom"]:
                names.append(filename)

    return names

def convert(directory, name):
    im = pydicom.dcmread(os.path.join(directory, name))
    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)
    return final_image

directory = sys.argv[1] if len(sys.argv) > 1 else DIR
names = get_names_of_imgs_inside_folder(directory)

for name in names:
    image = convert(directory, name)
    image.save(name+'.jpg')

    
