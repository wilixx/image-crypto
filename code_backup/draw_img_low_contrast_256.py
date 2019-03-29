from PIL import Image, ImageDraw, ImageFont
import numpy as np
# get an image
for i in range(1024):
# base = Image.open('Pillow/Tests/images/lena.png').convert('RGBA')

    color_back=(np.random.randint(255),
                np.random.randint(255),
                np.random.randint(255),
                0)
    print color_back
    color_fore=(color_back[0]+20,
                color_back[1]+20,
                color_back[2]+20,
                128)
    print color_fore
#     base = Image.new('RGBA', (128,128), (255,255,255,0))
    base = Image.new('RGBA', (128,128), color_back)
    
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, color_back)
#     txt = Image.new('RGBA', base.size, (255,255,255,0))
    
    # get a font
    # fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    fnt = ImageFont.truetype('SIMHEI.TTF', 40)
    fnt = ImageFont.truetype('SIMHEI.TTF', 128)
    # get a drawing context
    d = ImageDraw.Draw(txt)

# draw text, half opacity
# d.text(xy, text, fill, font, anchor)
# d.text((10,10), "Hello", font=fnt, fill=(105,22,25,128))

    number_i=""
    number_i=number_i+str(i)
    
    fig_id = np.random.randint(10)
    fig_number=""
    fig_number=fig_number+str(fig_id)
    d.text((30,3), fig_number, font=fnt, fill=color_fore)
# draw text, full opacity
# d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)

#     out.show()
    Image.Image.save(out, "number_low_contrast/number_"+number_i+".png", "png")
    print "Done"
    
    
    
    