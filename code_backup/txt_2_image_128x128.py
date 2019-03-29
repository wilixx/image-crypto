from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pickle
import numpy as np
import random
import glob
import sys,os
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
    base_color=(np.random.randint(1,255),
                np.random.randint(1,255),
                np.random.randint(1,255),
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
for i in range(256):
    back_ground=(np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255),
                0)
    back_ground=(255,
                 255,
                 255,
                0)
    print back_ground
    fore_ground=(back_ground[0]+1,
                    back_ground[1]+10,
                    back_ground[2]+10,
                    255)
    fore_ground=(255,
                    254,
                    255,
                    255)
    print fore_ground
        
    
    back_ground = (back_ground[0],back_ground[1],back_ground[2],255)
#     fore_ground = COLORS_OFF[idd*n_times]
    fore_ground = (fore_ground[0],fore_ground[1],fore_ground[2],255)
    
    print "back_ground",back_ground
    print "fore_ground",fore_ground
    

    txt = Image.new('RGBA', (128,128), back_ground)

    fnt = ImageFont.truetype('SIMHEI.TTF', 128)
    # get a drawing context
    d = ImageDraw.Draw(txt)
#     d.ellipse((1,1,127,127),back_ground)
#     d.ellipse((1,1,127,127),back_ground)

    number_i=""
    number_i=number_i+str(i)
    
    txt_number=random.randint(0,9)
    number_0_9=""
    number_0_9=number_0_9+str(txt_number)
    
#     label_number_color=(txt_number,txt_number,txt_number,255)
    d.text((30,3), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
#     Image.Image.save(txt, "info_image/number_"+number_i+".png", "png")
#     txt.save("number_img_test/number_"+number_i+".png")

################################################

    im=txt
    im=im
    base_color=(np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255),
                255)
    label_number_color=(base_color[0],base_color[1],base_color[2],txt_number)
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
    im.putpixel((im.size[0]-1,im.size[0]-1),label_number_color)
    print "new_color_map:",im.getcolors()
#     save_path="encod_image/"+os.path.split(im_path)[1]
#     print save_path
#     im.save("new_im.png")
#     im.save(save_path)
    im.save("training_set/number_"+number_i+".png")
    print "saved"
#     im.show()

    