from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pickle
import numpy as np
import random
import glob
import sys,os

data_volume = 7000
data_volume = 170
data_volume = 70000

base_17=["0","1","2","3","4","5","6","7",
         "8","9","A","B","C","D","E","F","G"]
labeled_data_path = "testing_data_7000"
unlabeled_data_path = "testing_data_7000_unlabeled"

labeled_data_path = "training_data_7000_0"
# unlabeled_data_path = "training_data_7000_0_unlabeled"
labeled_data_path = "training_data_7000_0_16base"

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
    save_path=unlabeled_data_path+r'/'+os.path.split(im_path)[1]
#     im.save("new_im.png")
    im.save(save_path)
    print "saved in",save_path
    print im_path,"unlabelize to",save_path

#     im.show()


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
    

    txt = Image.new('RGBA', (28,28), back_ground)

    fnt = ImageFont.truetype('SIMHEI.TTF', 26)
    # get a drawing context
    d = ImageDraw.Draw(txt)
#     d.ellipse((1,1,127,127),back_ground)
#     d.ellipse((1,1,127,127),back_ground)

    number_i=""
    number_i=number_i+str(i)
    
    txt_number=random.randint(0,16)
    txt_number_char=base_17[txt_number]
    number_0_9=""
#     number_0_9=number_0_9+str(txt_number)
    number_0_9=number_0_9+txt_number_char
    
#     label_number_color=(txt_number,txt_number,txt_number,255)


#     d.text((30,3), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    d.text((7,1), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    print "drawed text okay"
   
   #     Image.Image.save(txt, "info_image/number_"+number_i+".png", "png")
#     txt.save("number_img_test/number_"+number_i+".png")

################################################

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
    im.save(labeled_data_path+"/number_"+number_i+".png")
    print "saved"
#     im.show()

''' Unlabel operation
for im_path in glob.iglob(labeled_data_path+"/*"):
    unlabel_func(im_path)

print "done unlabeled"
'''
print "done training_data_prepare work all"

