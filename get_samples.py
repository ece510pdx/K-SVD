#import image data
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageFilter
from glob import glob
import random
import numpy as np
np.set_printoptions(threshold=np.nan)


def get_samples(path,samples,gray):
    
    if gray == 1:
    
    if gray == 0:
        result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.jpg'))] #create list of pictures
        #print(result)
        #create array of blocks
        i = 1
        j = 1
        result = result[:500] #only use first 500 images
        while j < samples:
            for x in result:
                img = x
                #print(img)
                img=mpimg.imread(img)
                #imgplot = plt.imshow(img)
                #plt.show()

                size_Y = img.shape
                M = size_Y[0]
                N = size_Y[1]

                x = random.randint(1,M-8) #chose a random x starting coordinate
                x2 = x+8
                y = random.randint(1,N-8) #choose a random y starting coordinate
                y2 = y+8
                
                block = img[x:x2,y:y2,0:3] #find an 8x8x3 block of image

                if i ==1: #make the first block all zeros
                    block_list = np.dot(block,0)
                    i = 2;
               
                block_list = np.concatenate((block_list, block), axis=0)
                j+=1
                #print(j)


    return block_list
