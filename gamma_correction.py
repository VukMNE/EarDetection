import cv2
import numpy as np
import glob
import os
from pathlib import Path
import json
from preprocessing.preprocess import Preprocess
import numpy as np
import cv2

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


preprocess = Preprocess()
images_path = 'data/ears/test'
new_images_path = 'data/ears/test_gamma/'

im_list = sorted(glob.glob(images_path + '/*.png', recursive=True))

for im_name in im_list:
    img = cv2.imread(im_name)
    img = adjust_gamma(img, 2)
    
    name_only = im_name.split('\\')[1]
    print(name_only)

    cv2.imwrite(new_images_path + name_only, img)

print('Done!')
