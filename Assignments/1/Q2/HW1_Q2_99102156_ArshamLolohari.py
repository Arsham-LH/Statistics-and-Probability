#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
from scipy.stats import bernoulli as ber

total = 100000 #total experiments
x = ber.rvs(p=0.01,size=total) #burglary event
y = np.array([0]*total) #alarm event
temp = 0
for i in range(total):
    if x[i]==1: #if burglary==true,
        temp = np.random.randint(1,101)
        if temp<=94:
            y[i]=1 #alarm is true with probability 0.94
    else:
        temp = np.random.randint(1,101)
        if temp==100:
            y[i]=1 #if burglary == flase, alarm is true with probability 0.01
s1,s2,s3=0,0,0 #si: total desired outcomes for probability pi
for i in range(total):
    if x[i]==1: # if burglary is true,
        if y[i]==1: #if alarm is true,
            s1=s1+1 #it's desired outcome for p1
        else:
            s3=s3+1 #it's desired outcome for p3
    else:
        if y[i]==1:
            s2=s2+1 #it's desired outcome for p2
        else:
            s3=s3+1 #it's desired outcome for p3
p1=s1/sum(x) #P(A=+a|B=+b)
p2=s2/(total-sum(x)) #P(A=+a|B=-b)
p3=s3/total #P(A=-a)

print(f"P(A=+a|B=+b) = {p1}")
print(f"P(A=+a|B=-b) = {p2}")
print(f"P(A=-a) = {p3}")

