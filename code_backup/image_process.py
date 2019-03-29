'''
Created on Mar 21, 2019

@author: Dr.Guo
'''
from PIL import Image

im=Image.open("grid_plate/grid_plate_2_5x5.png") 
im1=im.convert("L")
im1.show()











