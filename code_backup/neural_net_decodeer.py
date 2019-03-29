'''
Created on Mar 24, 2019

@author: Dr.Guo
'''
from PIL import Image
import glob
from distutils.msvc9compiler import NET_BASE
model = None
class model():
    net=None
    
    def parameter_modefiy(self,*kwargs):
        pass
    
    def train(self,training_set):
        pass

    def predict(self,image):
        '''return label
        '''
        pass
model = model()


'''Step-1 train_set and label_set preparation
'''
training_set = []
label_set = []
for im_path in glob.iglob("training_set/*"):
    training_set.append(im_path)
    
    im = Image.open(im_path)
    im_label = im.getpixel((im.size[0]-1,im.size[0]-1))[3]
    label_set.append(im_label)
    
for x,y in zip(training_set,label_set):
    print "{",x,y,"}"
    
'''Step-2 design and train a model
'''

'''Step-3 test model
'''
corret_count=0
for x,y in zip(training_set,label_set):
    
    print "{",x,y,"}"
    y_predict = model.predict(x)
    if y_predict==y:
        corret_count=corret_count=1
    
correct_rate = corret_count/len(training_set)





