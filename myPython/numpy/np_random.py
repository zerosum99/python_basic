# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:59:01 2016

@author: 06411
"""

import numpy as np


outcome = np.random.randint(1, 7, size=10)
print outcome, type(outcome), len(outcome)

print np.random.randint(2, size=10)
    
print np.random.randint(1, size=10)    
print np.random.randint(5, size=(2, 4))
 
#This is equivalent to np.random.randint(0,5,3) 
print np.random.choice(5, 3)
# p값은 선택되는 확률
# 0,1,2,3,4 의 확률
print np.random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0])

 
aa_milne_arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print np.random.choice(aa_milne_arr, 5, p=[0.5, 0.1, 0.1, 0.3])
   
a = np.random.choice(5, 3, replace=False)
print a
# a[4] = 10 IndexError: index 4 is out of bounds for axis 0 with size 3

print a
b = np.random.permutation(np.arange(5))[:3]
print b
#b[4] = 10 IndexError: index 4 is out of bounds for axis 0 with size 3

a = np.array([[1,2,3], [4,5,6]])
    
print np.cumsum(a)
print np.cumsum(a, dtype=float)     # specifies type of output value(s)
print np.cumsum(a,axis=0)      # sum over rows for each of the 3 columns
    
print np.cumsum(a,axis=1)      # sum over columns for each of the 2 rows


b = np.arange(12).reshape(3,4)
print b
print np.sum(b)
print np.sum(b,axis=0)                           # sum of each column
print np.sum(b,axis=1)                           # sum of each row
print np.cumsum(b,axis=1)                         # cumulative sum along each row
print np.cumsum(b,axis=0)                       # cumulative sum along each colum


weights = [0.2, 0.5, 0.3] 
cum_weights = [0] + list(np.cumsum(weights))
print(cum_weights)

print np.random.random_sample()

x = np.random.random_sample((3, 4))
print(x)
a = -3.4
b = 5.9
A = (b - a) * np.random.random_sample((3, 4)) + a
print(A)


