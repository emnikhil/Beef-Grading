"""
@author: NIKHIL GUPTA
"""

# Importing the Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Importing the Libraries for Image reading, cropping and saving
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

# Path for Input file and Output file
in_file = 'Beef Grading/Images/63-0713.jpg'
out_file = 'Beef Grading/sample.jpg' 

# Plotting the Input file
img = Image.open(in_file)
plt.imshow(img)


# setting the width and height of image as the original size of the image
width, height = img.size

#Change the values according to the image
# cropping the image to the desired size
# 1000 pixels from the left
# 180 pixels from the top
# 500 pixels from the right
# 600 pixels from the bottom
cropp = img.crop((1000, 180, width-500, height-600))
plt.imshow(cropp)
cropp.save(out_file)

# Converting the image to black and white
from matplotlib import cm
img = np.asarray(Image.open('Beef Images/sample.jpg').convert('L')) #read and convert image
img = 1 * (img < 127) # threshold


# Plotting the black and white image
plt.imshow(img, cmap=cm.Greys_r) # show as black and white
plt.show()

# Getting the size of image
m,n = img.shape

# Getting the pixels values of white and black pixels in the image
# use np.sum to count white pixels
print("{} white pixels, out of {} pixels in total.".format(img.sum(), m*n))

# 2% sub. from the white color percentage 
percentage = ((img.sum())/(m*n)*100)
print(percentage)
total_percentage = percentage- 2
print(total_percentage)

# Finding the category of the beef
if (100 - total_percentage) < 45.4 :
    print('Utility Grade Beef')
elif (100 - total_percentage) > 45.4 and (100 - total_percentage) < 47.7 :
    print('Select Grade Beef')
elif (100 - total_percentage) > 47.7 and (100 - total_percentage) < 50.0 :
    print('Choice Grade Beef')
elif (100 - total_percentage) > 50.0 and (100 - total_percentage) < 52.3 :
    print('Prime Grade Beef')
elif (100 - total_percentage) > 52.3 :
    print('Wagyu')
else:
    print('NaN')

