#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli as ber

p=0.4 #for bernoulli
total=10000 #maximum n
E=np.zeros(total)
Var=np.zeros(total)
Var_Y1=np.zeros(total)
Var_Y2=np.zeros(total)
Var_Y3=np.zeros(total)

for n in range(1,total+1): # for each n
    X1=ber.rvs(p,size=n) #defining Xi
    X2=ber.rvs(p,size=n)
    X3=ber.rvs(p,size=n)
    Y1=np.maximum(X1,X2) #defining Yi
    Y2=np.maximum(X2,X3)
    Y3=np.maximum(X3,X1)
    # for part 5
    Var_Y1[n-1]=np.var(Y1)
    Var_Y2[n-1]=np.var(Y2)
    Var_Y3[n-1]=np.var(Y3)
    
    Z=Y1+Y2+Y3 #defining Z
    #part 1
    E[n-1]=np.mean(Z)
    Var[n-1]=np.var(Z)
#parts 2 and 3, and 6 and 7
Var_Y_Sum=Var_Y1+Var_Y2+Var_Y3 # for part 6
Cml_avg_E=np.zeros(total)
Cml_avg_Var=np.zeros(total)
Cml_avg_Y_Sum=np.zeros(total)
for k in range(total):
    Cml_avg_E[k]=np.mean(E[:k+1]) #part 3
    Cml_avg_Var[k]=np.mean(Var[:k+1]) #part 4
    Cml_avg_Y_Sum[k]=np.mean(Var_Y_Sum[:k+1]) #part 7
#part 4
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle('Cml_avg_E & Cml_avg_Var vs n') #figure title
r=np.array(range(1,total+1)) #different values of n

plt.subplot(121) #for Cml_avg_E
plt.bar(r,Cml_avg_E,color='orange')
plt.ylabel('Cml_avg_E')
plt.xlabel('n')
plt.grid(True)

plt.subplot(122) #for Cml_avg_Var
plt.bar(r,Cml_avg_Var[r-1],color='orange')
plt.ylabel('Cml_avg_Var')
plt.xlabel('n')
plt.grid(True)
    
#part 8
fig = plt.figure(figsize=(15,6)) #creating figure
fig.suptitle('Cml_avg_Y_Sum vs n') #figure title
r=np.array(range(1,total+1)) #different values of n

plt.bar(r,Cml_avg_Y_Sum[r-1],color='blue')
plt.ylabel('Cml_avg_Y_Sum')
plt.xlabel('n')
plt.grid(True)

