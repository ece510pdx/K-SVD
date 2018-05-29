import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import numpy as np
from get_samples import get_samples


#get blocks of training data
samples = get_samples('lfw-deepfunneled',11000,1) #image folder path, # of samples to collect, 1 for grayscale)
print(samples)
samples_size = samples.shape
print(samples_size)


#create noisy picture
