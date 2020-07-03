#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import fashion_mnist
import numpy as np


# In[2]:


dataset = fashion_mnist.load_data()


# In[3]:


train , test = dataset


# In[4]:


X_train , y_train = train


# In[5]:


X_train = X_train.reshape(X_train.shape[0] , 28 ,28 ,1)


# In[6]:


X_test , y_test = test


# In[7]:


from keras.utils.np_utils import to_categorical


# In[8]:


y_train_cat = to_categorical(y_train)


# In[9]:


from keras.layers import Convolution2D


# In[10]:


from keras.layers import MaxPooling2D


# In[11]:


from keras.layers import Flatten


# In[12]:


from keras.models import Sequential


# In[13]:


from keras.layers import Dense


# In[14]:


model = Sequential()


# In[15]:


#model.add(Convolution2D(filters=32, 
#                        kernel_size=(3,3), 
#                        activation='relu',
#                   input_shape=(28,28,1)
#                      ))


# In[16]:


#model.add(MaxPooling2D(pool_size=(2, 2)))


# In[17]:


#model.add(Convolution2D(filters=32, 
#                        kernel_size=(3,3), 
#                        activation='relu',
#                       ))


# In[18]:


#model.add(MaxPooling2D(pool_size=(2, 2)))


# In[19]:


model.add(Flatten())


# In[20]:


model.add(Dense(units=512,  activation='relu'))


# In[21]:


#model.add(Dense(units=256, activation='relu'))


# In[22]:


#model.add(Dense(units=128, activation='relu'))


# In[23]:


#model.add(Dense(units=32, activation='relu'))


# In[24]:


model.add(Dense(units=10, activation='softmax'))


# In[ ]:





# In[25]:


from keras.optimizers import adam


# In[26]:


model.compile(optimizer='adam', loss='categorical_crossentropy', 
             metrics=['accuracy']
             )


# In[27]:


h = model.fit(X_train, y_train_cat, epochs=5)


# In[28]:


a = h.history['accuracy'][4]


# In[29]:


a = a.astype(str)


# In[30]:


file1 = open("accuracy.txt", "w")  


# In[31]:


file1.write(a)


# In[32]:


file1 = open('accuracy.txt', 'r') 
print(file1.read()) 
file1.close() 


# In[33]:


print(a)


# In[ ]:




