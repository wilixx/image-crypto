from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pickle
import numpy as np
COLORS_ON = []
COLORS_OFF = []
    
# color_pair = pickle.load(open( "d_colorPairs_40_done.pkl", "rb"))
# color_pair = pickle.load(open( "d_high_contrast_40.pkl", "rb"))
color_pair = pickle.load(open( "d_whole_map_50.pkl", "rb"))
print len(color_pair["colorset1"])
print color_pair["colorset1"]
color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

for color1 in color_pair["colorset1"]:
    COLORS_ON.append((int(color1[0]),int(color1[1]),int(color1[2])))
for color2 in color_pair["colorset2"]:
    COLORS_OFF.append((int(color2[0]),int(color2[1]),int(color2[2])))
  
print COLORS_OFF
print COLORS_ON

colorset_lenth = len(COLORS_OFF)
n_times = colorset_lenth//256
# get an image
for i in range(256):
#     idd= np.random.randint(256, size=1)
    idd= np.random.randint(colorset_lenth, size=1)
    idd = idd[0]
#     back_ground = COLORS_ON[idd*n_times]
    back_ground = COLORS_ON[idd]
    back_ground = (back_ground[0],back_ground[1],back_ground[2],255)
#     fore_ground = COLORS_OFF[idd*n_times]
    fore_ground = COLORS_OFF[idd]
    fore_ground = (fore_ground[0],fore_ground[1],fore_ground[2],255)
    
    print "back_ground",back_ground
    print "fore_ground",fore_ground
    
    base = Image.new('RGBA', (128,128), back_ground)
    base = Image.new('RGBA', (128,128), (255,255,255,0))
    
    # make a blank image for the text, initialized to transparent text color
#     txt = Image.new('RGBA', base.size, (15,126,255,0))
    txt = Image.new('RGBA', base.size, back_ground)
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    
    # get a font
    fnt = ImageFont.truetype('SIMHEI.TTF', 40)
    fnt = ImageFont.truetype('SIMHEI.TTF', 128)
    # get a drawing context
    d = ImageDraw.Draw(txt)
#     d.ellipse((1,1,127,127), back_ground, back_ground) 
#     d.ellipse((1,1,127,127), back_ground, (255,255,255,0))
    d.ellipse((1,1,127,127),back_ground)


# draw text, half opacity
# d.text(xy, text, fill, font, anchor)
# d.text((10,10), "Hello", font=fnt, fill=(105,22,25,128))

    number_i=""
    number_i=number_i+str(i)
    '''
    txt_number= np.random.randint(10, size=1)
    txt_number = txt_number[0]
    '''
    txt_number=idd%10
    number_0_9=""
    number_0_9=number_0_9+str(txt_number)
    
    
    d.text((30,3), number_0_9, font=fnt, fill=fore_ground)
# draw text, full opacity
# d.text((10,60), "World", font=fnt, fill=(255,255,255,255))
    '''
    '''
#     out = Image.alpha_composite(base, txt)
    '''
    txt.show()
#     txt=txt.filter(ImageFilter.SHARPEN)
#     txt.show()
#     out.show()
    '''
#     Image.Image.save(out, "number_img_test/number_"+number_i+".png", "png")
    Image.Image.save(txt, "d_dataset/number_"+number_i+".png", "png")
#     txt.save("number_img_test/number_"+number_i+".png")
print "Done 256 images"
    
    