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

labeled_data_path = "training_data_7000"
visible_data_path = "training_data_7000_visible"

labeled_data_path = "testing_data_7000"
visible_data_path = "testing_data_7000_visible"

# impath="number_low_contrast/number_1.png"
# print impath
# print os.path.split(impath)[1]
# save_path="number_high_contrast/"+os.path.split(impath)[1]
# print save_path
'''
im=Image.open("encod_image/number_12.png")

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
'''
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

def cmp_color(color1,color2):
    difference=[(value1-value2) for value1,value2 in zip(color1,color2)]
    sum_list=sum(difference)
    if sum_list>=0:
        return True
    else:
        return False

def decod_func(im_path):
#     im=Image.open("number_low_contrast/number_1.png")
    im=Image.open(im_path)
    im_height,im_width=im.size[0],im.size[1]
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
    color_map=((255,0,0,255),
               (255,128,0,255),
               (255,255,0,255),
               (0,255,0,255),
               (0,255,255,255),
               (0,0,255,255),
               (128,0,255,255),
                )
    color_bimap=((255,0,0,255),
               (255,128,0,255))
#     print base_color
    
    
    color_dict=im.getcolors()
#     print color_dict
#     print len(color_dict)
    label_number=im.getpixel((im.size[0]-1,im.size[0]-1))[3]
    label_color=im.getpixel((im.size[0]-1,im.size[0]-1))
    im.putpixel((im.size[0]-1,im.size[0]-1),im.getpixel((0,0)))
#     im.putpixel((0,0),base_color)
    for i in range(im_height):
        for j in range(im_width):
            color=im.getpixel((i,j))
#             print color
#             if cmp_color(color,im.getpixel((0,0))):
#                 im.putpixel((i,j),color_bimap[0])
#             else:
#                 im.putpixel((i,j),color_bimap[1])
#             if color>=im.getpixel((0,0)):
#                 im.putpixel((i,j),color_map[0])
#             if color==im.getpixel((0,0)):
#                 im.putpixel((i,j),color_map[1])
            try:
                if color==color_dict[0][1]:
                    im.putpixel((i,j),color_map[0])
                if color==color_dict[1][1]:
                    im.putpixel((i,j),color_map[1])
                if color==color_dict[2][1]:
                    im.putpixel((i,j),color_map[2])
                if color==color_dict[3][1]:
                    im.putpixel((i,j),color_map[3])
                if color==color_dict[4][1]:
                    im.putpixel((i,j),color_map[4])
                if color==color_dict[5][1]:
                    im.putpixel((i,j),color_map[5])
                if color==color_dict[6][1]:
                    im.putpixel((i,j),color_map[6])
            except:
                continue
    #         if color==color_dict[2][1]:
    #             im.putpixel((i,j),color_dict[2][1])
    im.putpixel((im.size[0]-1,im.size[0]-1),label_color)
    print "new_color_map:",im.getcolors()
    save_path=visible_data_path+"/"+os.path.split(im_path)[1]
#     im.save("new_im.png")
    im.save(save_path)
    print "saved in",save_path
    print im_path,"content is number",label_number

#     im.show()

for im_path in glob.iglob(labeled_data_path+"/*"):
    decod_func(im_path)
print "done all training_7000 to visible now"
