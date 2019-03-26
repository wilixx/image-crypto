'''Trains a simple convnet on the MNIST dataset.

Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from PIL import Image
import numpy as np
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
import matplotlib.pyplot as plt
from keras.models import load_model

'''My data loader
'''
x_train_all = []
y_train_all = []

# labeled_data_path = "training_data_7000_visible"
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
    
    x_train_all.append(im_array)
    y_train_all.append(y_lable)

print(len(x_train_all))
print(len(y_train_all))
x_train_all=np.array(x_train_all)
y_train_all=np.array(y_train_all)
print("Done load")
print(x_train_all.shape)
print(y_train_all.shape)
'''My data loader emd
'''

batch_size = 128
num_classes = 10
epochs = 12
epochs = 50
epochs = 26
# epochs = 5
# epochs = 1

'''Loss-print loader emd
'''
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = {'batch':[], 'epoch':[]}
        self.accuracy = {'batch':[], 'epoch':[]}
        self.val_loss = {'batch':[], 'epoch':[]}
        self.val_acc = {'batch':[], 'epoch':[]}

    def on_batch_end(self, batch, logs={}):
        self.losses['batch'].append(logs.get('loss'))
        self.accuracy['batch'].append(logs.get('acc'))
        self.val_loss['batch'].append(logs.get('val_loss'))
        self.val_acc['batch'].append(logs.get('val_acc'))

    def on_epoch_end(self, batch, logs={}):
        self.losses['epoch'].append(logs.get('loss'))
        self.accuracy['epoch'].append(logs.get('acc'))
        self.val_loss['epoch'].append(logs.get('val_loss'))
        self.val_acc['epoch'].append(logs.get('val_acc'))

    def loss_plot(self, loss_type):
        iters = range(len(self.losses[loss_type]))
        plt.figure()
        # acc
        plt.plot(iters, self.accuracy[loss_type], 'r', label='train acc')
        # loss
        plt.plot(iters, self.losses[loss_type], 'g', label='train loss')
        if loss_type == 'epoch':
            # val_acc
            plt.plot(iters, self.val_acc[loss_type], 'b', label='val acc')
            # val_loss
            plt.plot(iters, self.val_loss[loss_type], 'k', label='val loss')
        plt.grid(True)
        plt.xlabel(loss_type)
        plt.ylabel('acc-loss')
        plt.legend(loc="upper right")
        plt.savefig("loss_curve-50.png")
        plt.show()
        

'''Loss-print loader emd
'''


print("Hello start")
# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
'''
(x_train, y_train), (x_test, y_test) = mnist.load_data()
'''
x_train = x_train_all[0:6000]
x_test = x_train_all[6000:7000]
y_train = y_train_all[0:6000]
y_test =y_train_all[6000:7000]
# x_train,x_test=np.array(x_train),np.array(x_test)
# y_train,y_test=np.array(y_train),np.array(y_test)


print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))
# print(x_train[0])
# print(x_test[0])
# print(y_train[0:20])
# print(y_test[0:20])
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


if K.image_data_format() == 'channels_first':
#     x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
#     x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    x_train = x_train.reshape(x_train.shape[0], 3, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 3, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
#     x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
#     x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
#     input_shape = (img_rows, img_cols, 1)
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 3)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 3)
    input_shape = (img_rows, img_cols, 3)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
print("start construct model")

model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
'''Print model
'''
model.summary()
'''Print model
'''

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
print("compiled model")

history = LossHistory()

print("start fit model")
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test),
          callbacks=[history])
score = model.evaluate(x_test, y_test, verbose=0)
# load_model()
model.save_weights("model_W_img_crypto-unvisible-26.h5")
model.save("model_M_img_crypto-unvisible-26.h5")
print("Saved model to disk")
print('Test loss:', score[0])
print('Test accuracy:', score[1])

history.loss_plot('epoch')



