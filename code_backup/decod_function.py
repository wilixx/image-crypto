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
impath="number_low_contrast/number_1.png"
print impath
print os.path.split(impath)[1]
save_path="number_high_contrast/"+os.path.split(impath)[1]
print save_path
def enlarge_contrast(im_path):
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
    color_dict=im.getcolors()
    for i in range(128):
        for j in range(128):
            color=im.getpixel((i,j))
#             print color
            if color==color_dict[0][1]:
                pass
            if color==color_dict[1][1]:
                im.putpixel((i,j),color_dict[2][1])
    #         if color==color_dict[2][1]:
    #             im.putpixel((i,j),color_dict[2][1])
            if color==color_dict[2][1]:
                im.putpixel((i,j),(color[0]-50,color[1]-50,color[2]-50))
    #         im.putpixel((i,j),(128-color[0],128-color[1],128-color[2]))
#     print im.getcolors()
    save_path="number_high_contrast/"+os.path.split(im_path)[1]
    print save_path
#     im.save("new_im.png")
    im.save(save_path)
    print "saved"
#     im.show()

for im_path in glob.iglob("number_low_contrast/*"):
    enlarge_contrast(im_path)

