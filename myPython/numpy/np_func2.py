# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:33:07 2016

@author: 06411
"""

import numpy as np

def add(self,x,y) :
    return x+y
    
class A(object) :
    add= add
    
a = A()
print a.add(5,5)
print type(a.add)
print add(a,5,5)
print type(add)

#list에서 ndarray
a = [1,2,3]
b = np.tile(a,2)
print b
b = np.tile(a,(2,1))
print b
b = np.tile(a,(2,2))
print b

#1차원 ndarray에서 모형 형태 전환

a = np.array(a)
b = np.tile(a,(2,1))
print b

a = np.array(a)
b = np.tile(a,2)
print b