import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import numpy as np
from get_samples import get_samples
from noisy import noisy


#get blocks of training data
samples = get_samples('lfw-deepfunneled',11000,0) #image folder path, # of samples to collect,1 for isgrayscale)
print(samples)
samples_size = samples.shape
print(samples_size)


#path for full image to test on
path = '/Users/matthewkonyndyk/Desktop/K-SVD/lfw-deepfunneled/William_Genego/William_Genego_0001.jpg'

#original image
original_img=mpimg.imread(path)
imgplot = plt.imshow(original_img)
plt.show()

#depixelated image
noisy_img = noisy(path,100,1) #image path, r is the fraction of pixels to change to 0 per block
#img=mpimg.imread(noisy_img)
imgplot = plt.imshow(noisy_img)
plt.show()


#reshape images
noisy_img = np.reshape(noisy_img,187500) # for color images, 250x250x3 = 187500. Each 192 bit section corresponds to a block

