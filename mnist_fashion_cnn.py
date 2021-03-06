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


model.add(Flatten())

model.add(Dense(units=512,  activation='relu'))

model.add(Dense(units=10, activation='softmax'))

from keras.optimizers import adam

model.compile(optimizer='adam', loss='categorical_crossentropy', 
             metrics=['accuracy']
             )

e = 5
h = model.fit(X_train, y_train_cat, epochs=e)


a = h.history['accuracy'][-1]
a = a.astype(str)
file1 = open("accuracy.txt", "w")  
file1.write(a)
file1 = open('accuracy.txt', 'r') 
print(file1.read()) 
file1.close() 
print(a)
