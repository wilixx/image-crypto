'''
Created on Mar 24, 2019

@author: Dr.Guo
'''
'''
Created on Mar 17, 2019

@author: Dr.Guo
'''
'''
Created on Mar 17, 2019

@author: Dr.Guo
'''
import glob
from PIL import Image
import sys,os
import numpy as np
import random


def unlabel_func(im_path):
#     im=Image.open("number_low_contrast/number_1.png")
    im=Image.open(im_path)
    im_height,im_width=im.size[0],im.size[1]
#    
    
    
#     print color_dict
#     print len(color_dict)
    im.putpixel((im.size[0]-1,im.size[0]-1),im.getpixel((0,0)))
#     im.putpixel((0,0),base_color)
    print "new_color_map:",im.getcolors()
    save_path="unlabeled_training_data_28x28/"+os.path.split(im_path)[1]
#     im.save("new_im.png")
    im.save(save_path)
    print "saved in",save_path
    print im_path,"content is number",label_number

#     im.show()

for im_path in glob.iglob("training_data_28x28/*"):
    unlabel_func(im_path)

