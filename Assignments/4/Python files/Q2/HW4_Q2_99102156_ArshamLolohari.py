#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
from numpy.random import binomial as binom
from scipy.stats import norm
from math import sqrt

def SampleBinomial(p,n,size): #part1: creating SampleBinomial function
    return binom(n,p,size=size)
y=SampleBinomial(0.5,20,10000) #test for part1. expected mean:10, expected var:5
print("samples mean=",np.mean(y))
print("samples Var=",np.var(y))

#calculating probability(method1)
def FindProb(samples,l,u):
    N=len(samples) #samples size
    result=0 #number of elements inside interval [l,u]
    lowBound=np.where(samples>=l)  
    lowBound=lowBound[0] #index of elements greater or equal to l
    upBound=np.where(samples<=u)
    upBound=upBound[0] #index of elements lower or equal to u
    bound=np.intersect1d(lowBound,upBound) #common indices between upBound & lowBound
    result=len(bound)
    return result/N #final ratio

print("P(8<=Y<=10)= ", FindProb(y,8,10), "\t\t(using samples)") #testing function for l=8 & u=10



#calculating probability(method2)
def EstProb(p,n,l,u):
    mean=p #Bernoulli distribution expected value
    sd=sqrt(p*(1-p)) #Bernoulli distribution standard deviation
    return (norm.cdf((u-n*mean)/(sd*sqrt(n)))-norm.cdf((l-n*mean)/(sd*sqrt(n)))) #according to notes in report
print("P(8<=Y<=10)= ", EstProb(0.5,20.0,8.0,10.0), "\t\t(using CLT)") #testing function for l=8 & u=10



#calculating probability(method3)
def CorEstProb(p,n,l,u):
    mean=p #Bernoulli distribution expected value
    sd=sqrt(p*(1-p)) #Bernoulli distribution standard deviation
    return (norm.cdf((u+0.5-n*mean)/(sd*sqrt(n)))-norm.cdf((l-0.5-n*mean)/(sd*sqrt(n)))) #according to notes in report

print("P(8<=Y<=10)= ", CorEstProb(0.5,20.0,8.0,10.0), "\t\t(using continue correction)") #testing function for l=8 & u=10

