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
    back_ground=(np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255),
                255)
    
    print back_ground
    fore_ground=(back_ground[0]+20,
                    back_ground[1]+20,
                    back_ground[2]+20,
                    255)
    
    color_dict=im.getcolors()
    for i in range(128):
        for j in range(128):
            color=im.getpixel((i,j))
#             print color
            if color==color_dict[0][1]:
                im.putpixel((i,j),back_ground)
            if color==color_dict[1][1]:
                im.putpixel((i,j),fore_ground)
    #         if color==color_dict[2][1]:
    #             im.putpixel((i,j),color_dict[2][1])
    print "new_color_map:",im.getcolors()
    save_path="infom_image/"+os.path.split(im_path)[1]
    print save_path
#     im.save("new_im.png")
    im.save(save_path)
    print "saved"
#     im.show()

for im_path in glob.iglob("info_image/*"):
    encod_func(im_path)

