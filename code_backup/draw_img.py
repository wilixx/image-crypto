from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pickle
import numpy as np
import random
# COLORS_ON = []
# COLORS_OFF = []
# 
# color_back=(np.random.randint(255),
#                 np.random.randint(255),
#                 np.random.randint(255),
#                 0)
# print color_back
# color_fore=(color_back[0]+5,
#                 color_back[1]+5,
#                 color_back[2]+5,
#                 128)
# print color_fore
# colorset_lenth = len(COLORS_OFF)
# n_times = colorset_lenth//256
# get an image
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
    
#     base = Image.new('RGBA', (128,128), back_ground)
#     base = Image.new('RGBA', (128,128), (255,255,255,0))
    
    # make a blank image for the text, initialized to transparent text color
#     txt = Image.new('RGBA', base.size, (15,126,255,0))
    txt = Image.new('RGBA', (128,128), back_ground)
#     txt = Image.new('RGBA', base.size, (255,255,255,0))
    
    # get a font
#     fnt = ImageFont.truetype('SIMHEI.TTF', 40)
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
    
    
    d.text((30,3), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    Image.Image.save(txt, "info_image/number_"+number_i+".png", "png")
#     txt.save("number_img_test/number_"+number_i+".png")
print "Done 256 images"
    
    