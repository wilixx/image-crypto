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
# impath="number_low_contrast/number_1.png"
# print impath
# print os.path.split(impath)[1]
# save_path="number_high_contrast/"+os.path.split(impath)[1]
# print save_path

im=Image.open("info_image/number_12.png")

hi=im.histogram()
print hi
print im.size
print im.palette
print im.getcolors()
print len(im.getcolors())
print len(hi)
print sum(hi),128*128
print random.randrange(3)
print random.randrange(3)
print random.randrange(3)
print random.randrange(3)
print random.randrange(3)
print random.randrange(3)
print random.randrange(3)

def color_plus_1(base_color):
    i = random.randrange(3)
    back_grounder=[item for item in base_color]
    back_grounder[i]=back_grounder[i]+1
    back_grounder=(back_grounder[0],back_grounder[1],back_grounder[2],back_grounder[3])
    return back_grounder

def color_minus_1(base_color):
    i = random.randrange(3)
    back_grounder=[item for item in base_color]
    back_grounder[i]=back_grounder[i]-1
    back_grounder=(back_grounder[0],back_grounder[1],back_grounder[2],back_grounder[3])
    return back_grounder
# color_test=back_color([10,5,6])
# print color_test
# color_test=back_color([20,5,6])
# print color_test
# color_test=back_color([40,5,6])
# print color_test
# color_test=back_color([10,50,6])
# print color_test

def encod_func(im_path):
#     im=Image.open("number_low_contrast/number_1.png")
    im=Image.open(im_path)
#     os.path.split()
    '''
    hi=im.histogram()
    print hi
    print im.size
    print im.palette
    print im.getcolors()
    print len(hi)
    print sum(hi),128*128
    '''
    base_color=(np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255),
                255)
    
    print base_color
    
    
    
    color_dict=im.getcolors()
    im.putpixel((0,0),base_color)
    for i in range(128):
        for j in range(128):
            color=im.getpixel((i,j))
#             print color
            if color==color_dict[0][1]:
                im.putpixel((i,j),color_plus_1(base_color))
            if color==color_dict[1][1]:
                im.putpixel((i,j),color_minus_1(base_color))
    #         if color==color_dict[2][1]:
    #             im.putpixel((i,j),color_dict[2][1])
    print "new_color_map:",im.getcolors()
    save_path="encod_image/"+os.path.split(im_path)[1]
    print save_path
#     im.save("new_im.png")
    im.save(save_path)
    print "saved"
#     im.show()

for im_path in glob.iglob("infom_image/*"):
    encod_func(im_path)

