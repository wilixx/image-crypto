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


#     im.show()
for i in range(256):
    back_ground=(np.random.randint(1,255),
                np.random.randint(1,255),
                np.random.randint(1,255),
                0)
    back_ground=(255,
                 0,
                 255,
                0)
    print back_ground
    fore_ground=(back_ground[0]+1,
                    back_ground[1]+10,
                    back_ground[2]+10,
                    255)
    fore_ground=(105,
                    54,
                    0,
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
    
    txt_number=random.randint(0,9)
    number_0_9=""
    number_0_9=number_0_9+str(txt_number)
    
#     label_number_color=(txt_number,txt_number,txt_number,255)


#     d.text((30,3), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    d.text((7,1), number_0_9, font=fnt, fill=fore_ground,outline=fore_ground)
    print "drawed text okay"
   
    Image.Image.save(txt, "training_data_28x28/number_"+number_i+".png", "png")
#     txt.save("number_img_test/number_"+number_i+".png")

################################################

#     im=txt
#     im.save("training_data_28x28/number_"+number_i+".png")
    print "saved"
#     im.show()

    