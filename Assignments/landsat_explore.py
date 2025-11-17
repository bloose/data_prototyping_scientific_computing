#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 29 12:36:18 2021

@author: Brice


"""
import json
import matplotlib.pyplot as plt
from skimage import io


img = io.imread(S['display_id']+'_B4.TIF')

#%%   Fill the rest in yourself using your past graphing experience.
# make a figure object plot
fig = plt.figure()


# Use plt.imshow() to display the landsat image.  
plt.imshow(img)
plt.show()

# Verify that you captured Rhode Island and Narragansett Bay in the image.

# Because we can't display figure objects on Oscar, save the figure to a file.
fig.savefig('lsexplore.png')
print('Image save complete')


