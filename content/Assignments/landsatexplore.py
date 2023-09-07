#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25, 2021

@author: 


# More detail on landsatexplore at 
	https://github.com/yannforget/landsatxplore

 
"""

import json
from landsatxplore.api import API
import matplotlib.pyplot as plt
from skimage import io
from landsatxplore.earthexplorer import EarthExplorer


# Visit https://ers.cr.usgs.gov/register to create an account.
username=''
password=''

# Initialize a new API instance and a new EarthExplorer instance, using your 
# username and password.
api = API(username, password)
ee = EarthExplorer(username, password)


# Search for Landsat TM scenes
scenes = api.search(
    dataset='landsat_tm_c1',
    latitude=41,
    #Specify the longitude of RI 
    #longitude=,
    start_date='1995-01-01',
    #Specify  end_date
    max_cloud_cover=5
)

print(f"{len(scenes)} scenes found.")


# Grab the first scene (you can change this) and download it.  Note
# the file downloads with a unix compression format called .tar.gz.  It is similar
# to a .zip file.
S = scenes[0]

# We can use the landsat api geojson variable 'display_id' to download the file.
ee.download(S['display_id'],'./')


# Use the OS library to execute a command in the terminal.  You will unzip all the files
# ending in .gz
import os
os.system("tar -xvf *.gz")
img = io.imread(S['display_id']+'_B4.TIF')


#%%   Fill the rest in yourself using your past graphing experience.
# make a figure object plot
fig = plt.figure()


# Use plt.imshow() to display the landsat image.  
plt.imshow(img)
plt.show()

# Verify that you captured Rhode Island and Narragansett Bay in the image.

# Because we can't display figure objects on Oscar, save the figure to a file so you 
# can download with sftp.

print('Image save complete')


