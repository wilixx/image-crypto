'''
Created on Mar 25, 2019

@author: Dr.Guo
'''
from PIL import Image,ImageFilter
import glob
import os
labeled_data_path = "gray_v_image"
save_data_path = "contour_dataset"
for im_path in glob.iglob(labeled_data_path+"/*"):
    img=Image.open(im_path)
    print im_path
    filename=os.path.split(im_path)[1]
    print filename
    img=img.filter(ImageFilter.CONTOUR)
    img.save(save_data_path+"/"+filename)
    
    
    
    