from PIL import Image, ImageDraw, ImageFont
import numpy as np

base_17=["0","1","2","3","4","5","6","7",
         "8","9","A","B","C","D","E","F","G"]
# get an image
for i in range(1024):
# base = Image.open('Pillow/Tests/images/lena.png').convert('RGBA')
    base = Image.new('RGBA', (128,128), (255,255,255,0))
    base = Image.new('RGBA', (128,128), (15,126,255,0))
    
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (15,126,255,0))
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
    d.text((30,3), fig_number, font=fnt, fill=(105,22,25,128))
# draw text, full opacity
# d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)

#     out.show()
    Image.Image.save(out, "number_low_contrast/number_"+number_i+".png", "png")