'''
Created on Mar 25, 2019

@author: Dr.Guo
'''
import numpy as np
def generator_1_255():
    num=np.random.randint(1,255)
#     print np.random.randint(1,255)
    return num

count_1=0
count_254=0
count_128=0
for i in range(100):
    num=generator_1_255()
    if num == 1:
        count_1=count_1+1
    if num == 254:
        count_254=count_254+1
    if num == 128:
        count_128=count_128+1
        
print count_1
print count_254
print count_128















