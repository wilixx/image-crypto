'''
Created on Mar 17, 2019

@author: Dr.Guo
'''
'''
Created on Mar 17, 2019

@author: Dr.Guo
'''
from PIL import Image

im=Image.open("number_low_contrast/number_1.png")
hi=im.histogram()
print hi
print im.size
print im.palette
print im.getcolors()
print len(hi)
print sum(hi),128*128

color_dict=im.getcolors()
for i in range(128):
    for j in range(128):
        color=im.getpixel((i,j))
        print color
        if color==color_dict[0][1]:
            pass
        if color==color_dict[1][1]:
            im.putpixel((i,j),color_dict[2][1])
#         if color==color_dict[2][1]:
#             im.putpixel((i,j),color_dict[2][1])
        if color==color_dict[2][1]:
            im.putpixel((i,j),(color[0]-50,color[1]-50,color[2]-50))
#         im.putpixel((i,j),(128-color[0],128-color[1],128-color[2]))
print im.getcolors()
im.save("new_im.png")
im.show()


