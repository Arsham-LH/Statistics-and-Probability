#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
from numpy.random import exponential as expon
from math import ceil
from math import exp
from math import factorial as fact
import matplotlib.pyplot as plt
from scipy.stats import poisson


landa=0.3 #landa in exponential random variable
total = 1000 #total samples
X=expon(1/landa,total) #creating a vector containing 1000 expoential distribution samples
lastCallTime=sum(X)
lastSecond=ceil(lastCallTime) #the last second to check, according to the last call time
def callTime(X,index): #the time of call, given samples vector X & the corresponding index for that call
    return sum(X[:index+1])

callsNum = np.zeros(lastSecond) #result vector
callsTimes=np.zeros(total)
for i in range(total):
    callsTimes[i]=callTime(X,i)
newSum=0
for i in range(lastSecond):
    for j in range(total):
        newSum=callsTimes[j]
        if i==lastSecond-1: #if we're in the last loop
            if newSum>i+1: #if our sum exceeds i+1, we won't have any call in the interval anymore
                break
            elif newSum>=i and newSum<=i+1: #last interval is like [i,i+1]
                callsNum[i]=callsNum[i]+1 #call has happenned in current interval
        else:
            if newSum>=i+1:
                break
            elif newSum>=i and newSum<i+1: #all intervals except last one is like [i,i+1)
                callsNum[i]=callsNum[i]+1



fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle('callsNum normalized histogram + real poisson PMF') #figure title
maxNum=int(max(callsNum)) #maximum number of calls in an interval
plt.hist(callsNum,range=(0,maxNum+1),bins=range(0,maxNum+1),rwidth=1,density=True)
plt.ylabel('frequecy(normalized) / PMF')
plt.xlabel('calls number / k')
plt.grid(True)

# xPoints=np.array(range(0,7))
# yPoints=np.zeros(len(xPoints))
# for i in range(len(xPoints)):
#     yPoints[i]=exp(-landa)*(landa**xPoints[i])/fact(int(xPoints[i]))
r=range(0,7)
Y=poisson(mu=landa)
poissPlot=plt.bar(r,Y.pmf(r),width=0.5,color='orange')

plt.show()
    

