#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist
import numpy as np


# In[2]:


dataset = mnist.load_data('mymnist.db')


# In[3]:


train , test = dataset


# In[4]:


X_train , y_train = train


# In[ ]:


X_train.shape


# In[ ]:


X_train = X_train.reshape(X_train.shape[0] , 28 ,28 ,1)


# In[ ]:


X_test , y_test = test


# In[ ]:


X_test.shape


# In[ ]:


X_train.shape


# In[ ]:


X_train.shape


# In[ ]:


y_train.shape


# In[ ]:


from keras.utils.np_utils import to_categorical


# In[ ]:


y_train_cat = to_categorical(y_train)


# In[ ]:


y_train_cat


# In[ ]:


y_train_cat[7]


# In[ ]:


from keras.layers import Convolution2D


# In[ ]:


from keras.layers import MaxPooling2D


# In[ ]:


from keras.layers import Flatten


# In[ ]:


from keras.models import Sequential


# In[ ]:


from keras.layers import Dense


# In[ ]:


model = Sequential()


# In[ ]:


model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(28,28,1)
                       ))


# In[ ]:


model.add(MaxPooling2D(pool_size=(2, 2)))


# In[ ]:


#model.add(Convolution2D(filters=32, 
 #                       kernel_size=(3,3), 
  #                      activation='relu',
   #                    ))


# In[ ]:


#model.add(MaxPooling2D(pool_size=(2, 2)))


# In[ ]:


model.add(Flatten())


# In[ ]:


model.add(Dense(units=512, input_dim=28*28, activation='relu'))


# In[ ]:


#model.add(Dense(units=256, activation='relu'))


# In[ ]:


#model.add(Dense(units=128, activation='relu'))


# In[ ]:


#model.add(Dense(units=32, activation='relu'))


# In[ ]:


model.add(Dense(units=10, activation='softmax'))


# In[ ]:


model.summary()


# In[ ]:


from keras.optimizers import RMSprop


# In[ ]:


model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )


# In[39]:


h = model.fit(X_train, y_train_cat, epochs=1)


# In[ ]:


plt.imshow(X_test[0])


# In[ ]:


y_test[0]


# In[ ]:


model.predict(X_test[0])


# In[ ]:


test_img = X_test[0].reshape(28*28)


# In[ ]:


test_img.shape


# In[ ]:


model.predict(test_img)


# In[ ]:




