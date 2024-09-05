#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
df=pd.read_csv("heart.csv") #reading excel file
print(df.head()) #printing first 5 rows
print(df.info()) #printing some info


# In[20]:


df_chol=df['chol']
print(df_chol.describe())
#print(np.mean(df_chol))


# In[91]:


import matplotlib.pyplot as plt

mean=np.mean(df_chol)

fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle("'chol' histogram & mean(red line)") #figure title
plt.hist(df_chol,range=(min(df_chol),max(df_chol)),bins=100) #plotting histogram, bins number=100, range from minimum chol to max
plt.ylabel('frequency')
plt.xlabel('chol')
plt.grid(True)
plt.bar(mean,20,color="red") #showing mean with a red line

print(mean)


# In[96]:


from random import sample

def SamplesMean(arr,size): #defining a function to calculate mean
    samp=sample(arr,size)
    return np.mean(samp)
size=30 #number of samples
N=300 #total experiments
means=np.zeros(N)
for i in range(N):
    means[i]=SamplesMean(list(df_chol),size)
    
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle("means histogram (samples size=30)") #figure title
plt.hist(means,bins=100) #plotting histogram, bins number=100
plt.ylabel('frequency')
plt.xlabel('mean')
plt.grid(True)


# In[93]:


from random import sample

def SamplesMean(arr,size): #defining a function to calculate mean
    samp=sample(arr,size)
    return np.mean(samp)
size=20 #number of samples
N=300 #total experiments
means=np.zeros(N)
for i in range(N):
    means[i]=SamplesMean(list(df_chol),size)
    
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle("means histogram (samples size=20)") #figure title
plt.hist(means,bins=100) #plotting histogram, bins number=100
plt.ylabel('frequency')
plt.xlabel('mean')
plt.grid(True)


# In[103]:


from random import sample

def SamplesMean(arr,size): #defining a function to calculate mean
    samp=sample(arr,size)
    return np.mean(samp)
size=60 #number of samples
N=300 #total experiments
means=np.zeros(N)
for i in range(N):
    means[i]=SamplesMean(list(df_chol),size)
    
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle("means histogram (samples size=60)") #figure title
plt.hist(means,bins=100) #plotting histogram, bins number=100
plt.ylabel('frequency')
plt.xlabel('mean')
plt.grid(True)


# In[105]:


from random import sample

def SamplesMean(arr,size): #defining a function to calculate mean
    samp=sample(arr,size)
    return np.mean(samp)
size=100 #number of samples
N=300 #total experiments
means=np.zeros(N)
for i in range(N):
    means[i]=SamplesMean(list(df_chol),size)
    
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle("means histogram (samples size=100)") #figure title
plt.hist(means,bins=100) #plotting histogram, bins number=100
plt.ylabel('frequency')
plt.xlabel('mean')
plt.grid(True)

