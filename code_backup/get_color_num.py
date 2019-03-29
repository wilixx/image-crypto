'''
Created on Mar 21, 2019

@author: Dr.Guo
'''
from PIL import Image

im_path="grid_plate/grid_plate_2_5x5.png"
im=Image.open(im_path)
#     os.path.split()
    
hi=im.histogram()
print hi
print im.size
print im.palette
print im.getcolors()
print len(im.getcolors())
print 7*5*5










