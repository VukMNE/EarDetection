import cv2
import numpy as np
import glob
import os
from pathlib import Path
import json
from preprocessing.preprocess import Preprocess


preprocess = Preprocess()
images_path = 'data/ears/test'
new_images_path = 'data/ears/test_hist/'

im_list = sorted(glob.glob(images_path + '/*.png', recursive=True))

for im_name in im_list:
    img = cv2.imread(im_name)
    img = preprocess.histogram_equlization_rgb(img)
    
    name_only = im_name.split('\\')[1]
    print(name_only)

    cv2.imwrite(new_images_path + name_only, img)

print('Done!')
