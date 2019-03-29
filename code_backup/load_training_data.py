'''
Created on Mar 24, 2019

@author: Dr.Guo
'''
from PIL import Image
import glob
from distutils.msvc9compiler import NET_BASE
from time import sleep
import numpy as np

'''Step-1 train_set and label_set preparation
'''
x_train = []
y_train = []

labeled_data_path = "training_data_7000"
unlabeled_data_path = "training_data_7000_unlabeled"
data_volume=7000
i=0
im_path=labeled_data_path+"/number_"+str(i)+".png"
im = Image.open(im_path)
y_lable=im.getpixel((im.size[0]-1,im.size[0]-1))[3]
# print im.mode
im=im.convert("RGB")
print im.mode
# im.convert()
im_array=np.asarray(im)
# print im_array
# print y_lable
'''
x_train.append(im_array)
y_train.append(y_lable)

print x_train
print y_train
'''
for i in range(data_volume):
    im_path=labeled_data_path+"/number_"+str(i)+".png"
    im = Image.open(im_path)
    y_lable=im.getpixel((im.size[0]-1,im.size[0]-1))[3]
#     print im.mode
    im=im.convert("RGB")
#     print im.mode
    # im.convert()
    im_array=np.asarray(im)
    
    x_train.append(im_array)
    y_train.append(y_lable)
 
print x_train[0]   
print y_train[0:20]   
print len(x_train)
print len(y_train)
'''
for im_path in glob.iglob(labeled_data_path+"/*"):
    training_set_28.append(im_path)
    
    im = Image.open(im_path)
    im_label = im.getpixel((im.size[0]-1,im.size[1]-1))[3]
    label_set_28.append(im_label)
    
for x,y in zip(training_set_28,label_set_28):
    print "{",x,y,"}"
    
for im_path in glob.iglob(unlabeled_data_path+"/*"):
    training_set.append(im_path)
    
    im = Image.open(im_path)
    im_label = im.getpixel((im.size[0]-1,im.size[1]-1))[3]
    label_set.append(im_label)
    
for x,y in zip(training_set,label_set):
    print "{",x,y,"}"

# sleep(1)
for i in range(10):
    print len(training_set)
    print len(label_set)
# 
# for x,y in zip(label_set,label_set_28):
#     print "{",x,y,"}"

'''
