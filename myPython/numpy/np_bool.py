# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:34:19 2016

@author: 06411
"""

import numpy as np

ba = np.array([True,False,True],dtype=np.bool)
print ba, type(ba)

b = np.bool_([True,False,True])
print b, type(ba)
print b.ndim 
print b.__class__.mro()
'''
for k, v in np.bool_.__dict__.items() :
    if callable(v) :
        pass
    else :
        print k
        
i = np.int_([1,2,3])
print i, type(i)
'''
for k, v in np.__dict__.items() :
    if callable(v) :
        print k
    else :
        pass
        
z = np.arange(3, dtype=np.uint8)
print z

