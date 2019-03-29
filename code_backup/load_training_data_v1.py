'''
Created on Mar 24, 2019

@author: Dr.Guo
'''
from PIL import Image
import glob
from time import sleep
import numpy as np

x_train = []
y_train = []

labeled_data_path = "training_data_7000"
data_volume=7000

for i in range(data_volume):
    im_path=labeled_data_path+"/number_"+str(i)+".png"
    im = Image.open(im_path)
    y_lable=im.getpixel((im.size[0]-1,im.size[0]-1))[3]
#     print im.mode
    im=im.convert("RGB")
#     print im.mode
    im_array=np.asarray(im)
    
    x_train.append(im_array)
    y_train.append(y_lable)
x_train=np.array(x_train)
y_train=np.array(y_train)
print x_train[0]   
print y_train[0:20]   
print len(x_train)
print len(y_train)
print x_train.shape
print y_train.shape