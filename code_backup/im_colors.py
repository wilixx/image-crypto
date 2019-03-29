'''
Created on Mar 17, 2019

@author: Dr.Guo
'''
from PIL import Image

im=Image.open("number_low_contrast/number_0.png")
hi=im.histogram()
print hi
print im.size
print im.palette
print len(hi)
print sum(hi),128*128



