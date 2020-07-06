#!/usr/bin/env python
# coding: utf-8

from keras.datasets import fashion_mnist
import numpy as np
dataset = fashion_mnist.load_data()

train , test = dataset
X_train , y_train = train
X_train = X_train.reshape(X_train.shape[0] , 28 ,28 ,1)
X_test , y_test = test
from keras.utils.np_utils import to_categorical
y_train_cat = to_categorical(y_train)

from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

#model.add(Convolution2D(filters=32, 
#                        kernel_size=(3,3), 
#                        activation='relu',
#                   input_shape=(28,28,1)
#                      ))


#model.add(MaxPooling2D(pool_size=(2, 2)))

#model.add(Convolution2D(filters=32, 
#                        kernel_size=(3,3), 
#                        activation='relu',
#                       ))


#model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
unit = 512
model.add(Dense(units=unit,  activation='relu'))

#model.add(Dense(units=256, activation='relu'))

#model.add(Dense(units=128, activation='relu'))

#model.add(Dense(units=32, activation='relu'))

model.add(Dense(units=10, activation='softmax'))

from keras.optimizers import adam

model.compile(optimizer='adam', loss='categorical_crossentropy', 
             metrics=['accuracy']
             )

epoch = 5
h = model.fit(X_train, y_train_cat, epochs=epoch)


a = h.history['accuracy'][4]
a = a.astype(str)
file1 = open("accuracy.txt", "w")  
file1.write(a)
file1 = open('accuracy.txt', 'r') 
print(file1.read()) 
file1.close() 
print(a)
