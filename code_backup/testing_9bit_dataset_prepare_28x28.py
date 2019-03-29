from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pickle
import numpy as np
import random
import glob
import sys,os

data_volume = 70000
data_volume = 9000

labeled_data_path = "testing_data_9_bit_9000"
# unlabeled_data_path = "training_data_7000_0_unlabeled"

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

for i in range(data_volume):
    back_ground=(np.random.randint(1,255),
                np.random.randint(1,255),
                np.random.randint(1,255),
                0)
    back_ground=(255,
                 255,
                 255,
                0)
    print back_ground
    fore_ground=(back_ground[0]+1,back_ground[1]+10,back_ground[2]+10,
                    255)
    fore_ground=(255,
                    254,
                    255,
                    255)
    print fore_ground
        
    back_ground = (back_ground[0],back_ground[1],back_ground[2],255)
    fore_ground = (fore_ground[0],fore_ground[1],fore_ground[2],255)
    
    print "back_ground",back_ground
    print "fore_ground",fore_ground
    

    txt = Image.new('RGBA', (28,28), back_ground)

    fnt = ImageFont.truetype('SIMHEI.TTF', 26)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    number_i=""
    number_i=number_i+str(i)
    if (i%3==0):
        txt_number=random.randint(0,9)
    number_0_9=""
    number_0_9=number_0_9+str(txt_number)
    
    d.text((7,1), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    print "drawed text okay"
   

    im=txt
    im=im
    base_color=(np.random.randint(1,255),
                np.random.randint(1,255),
                np.random.randint(1,255),
                255)
    label_number_color=(base_color[0],base_color[1],base_color[2],txt_number)
    print base_color
    
    color_dict=im.getcolors()
    print "origin color number=",len(color_dict)
    im.putpixel((0,0),base_color)
    
    for i in range(28):
        for j in range(28):
            color=im.getpixel((i,j))
            if color==color_dict[0][1]:
                im.putpixel((i,j),color_plus_1(base_color))
            if color==color_dict[1][1]:
                
                im.putpixel((i,j),color_minus_1(base_color))
    im.putpixel((im.size[0]-1,im.size[0]-1),label_number_color)
    print "new_color_map:",im.getcolors()
    im.save(labeled_data_path+"/number_"+number_i+".png")
    print "saved"
#     im.show()

print "done training_data_prepare work all"

