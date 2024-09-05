#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
from scipy.stats import cauchy


def CauchySampling(x0,gamma,size): #defining function
    y=np.array(cauchy.rvs(loc=x0, scale=gamma, size=size)) #sampling from cauchy distribution
    return np.mean(y) #calculating mean
loc=100 #test x0
scale=10 #test gamma
size=100 #size for rvs
test=CauchySampling(loc,scale,size)
print("test=",test)
N=1000 #total number of tests
y=np.zeros(N)
for i in range(0,N): #testing N times and calculating means
    y[i]=CauchySampling(loc,scale,size)
var=np.var(y) #calculating variance
print("Var(y)=",var)


# In[57]:


import numpy as np
from scipy.stats import pareto


def ParetoSampling(xm,alpha,size): #defining function
    y=np.array(pareto.rvs(b=alpha, loc=0, scale=xm, size=size)) #sampling from pareto distribution
    return np.mean(y) #calculating mean
scale=1 #test xm
b=0.5 #test alpha(shape)
size=100 #size for rvs
test=ParetoSampling(scale,b,size)
print("test=",test)
N=1000 #total number of tests
n=np.zeros(N)
for i in range(0,N): #testing N times and calculating means
    n[i]=ParetoSampling(scale,b,size)
var=np.var(n) #calculating variance
print("Var(n)=",var)

