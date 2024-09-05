#!/usr/bin/env python
# coding: utf-8

# In[23]:


from math import pi as pi
from math import sin as sin
import numpy as np
from scipy.stats import bernoulli as ber

total = 100000 # total experiments
l = 5 #lines distance
L = 1 #needle length
result = np.array([0]*total) # array of experiments results, one if lies across a line, zero otherwise

x = np.random.uniform(0,5,total) #needles center from previous line
theta = np.random.uniform(0,pi,total) #angle with lines
for i in range(total):
    if (x[i]+L/2*sin(theta[i]))>=l or (x[i]-L/2*sin(theta[i]))<=0: #if needle and line intersect
        result[i] = 1
p = sum(result)/total #the probability

pi_app = 2*L/(l*p) #our approximation of pi number
print(pi_app)

        


# In[ ]:




