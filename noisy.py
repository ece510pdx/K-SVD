#import image data
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from glob import glob
import random
import numpy as np
np.set_printoptions(threshold=np.nan)

#adds noise to an image
def noisy(path,r,isgrayscale): #folder path for jpg images, # of samples to collect, 1 for grayscale 0 for rbg
    if isgrayscale == 0: #if color
       #adds noise to color image
       #img = path
        #print(img)
        img=mpimg.imread(path)
        img = img.copy()
        original = img.copy()
        #print(img)
        #imgplot = plt.imshow(img)
        #plt.show()
        
        size_Y = img.shape
        M = size_Y[0]
        N = size_Y[1]
        Z = size_Y[2]
        #print(M,N,Z)
        
        counter = r/100*64
        
        while counter > 0:
            for x in range (0,M-8,8):
                for y in range (0,N-8,8):
                    a = x + random.randint(0,7)
                    b = y + random.randint(0,7)
                    #print(a,b)
                    img[a,b,0] = 0
                    img[a,b,1] = 0
                    img[a,b,2] = 0
            counter -= 1



    if isgrayscale == 1: #if grayscale
        #adds noise to color image
        #img = path
        #print(img)
        img=mpimg.imread(path)
        img = img.copy()
        original_img = img.copy()
        #print(img)
        #imgplot = plt.imshow(img)
        #plt.show()
    
        size_Y = img.shape
        M = size_Y[0]
        N = size_Y[1]
        
        counter = r/100*64
        
        while counter > 0:
            for x in range (0,M-8,8):
                for y in range (0,N-8,8):
                    
                    a = x + random.randint(0,7)
                    b = y + random.randint(0,7)
                    #print(a,b)
                    img[a,b,0] = 0
                    img[a,b,1] = 0
            counter -= 1

    #imgplot = plt.imshow(img)
    #plt.show()

    noisy_img = img
    return noisy_img
