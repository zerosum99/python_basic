# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:12:47 2016

@author: 06411
"""

import numpy as np
import pandas as pd

print(np.random.randn(5))
s = pd.Series([0,1,2,3,4])

s1 = pd.Series([0,1,2,3,4], index=['a', 'b', 'c', 'd', 'e'])

print(s, type(s))
print(s1, type(s1))

print(s.index, s[0])
print(s1.index,s1['a'])

print(s[0:3])
print(s1['a':'c'])

print(s[s<3])
print(s1[s1>3])

print(s[[4,3,1]])
print(s1[['d','a','c']])

d = {'a':1,'b':2,'c':3}
s2 = pd.Series(d)
print(s2)

print(s2.get('d'))
print(s2.get('d',np.nan))

print(s2 + 1)
print(s2 - 1)
print(s2 * 3)
print(s2 / 2)
print(s2 // 2)
print(s2 % 2)

print(s2 + s2)
print(s2 + s2[0:2])


d = {'a':1,'b':2,'c':3}
s3 = pd.Series(d,name='something')
print(s3, s3.name)

print(s3.shape)
print(s3.dtypes)
print(s3.ndim)
print(s3.blocks)
print(s3.values)
print(s3.ix, s3.ix[0])
print(s3.at, s3.at['a'])
print(s3.iat, s3.iat[0])

print(s3.size)
print(s3.T)
print("strides",s3.strides)
print(s3.base)

print(s3.dtypes)
s4 =s3.astype(np.float64).rename('dahl')
print(s4,s4.dtypes)