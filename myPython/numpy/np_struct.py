# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:24:03 2016

@author: 06411
"""

import numpy as np
import inspect

x = np.array([(1,2.,'Hello'), (2,3.,"World")], 
dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')]) 
print x
 
print x[0]
print x[0]['foo']
print x[0]['bar']
print x[0]['baz']

print x['foo']
print x['bar']
print x['baz']


y = x['foo']
print y
y[:] = 2*y
print y
print x['foo']

z = np.zeros(3)
print z
print z.dtype
z23 = np.zeros((2,3))
print z23, type(z23)
print z23.dtype
xz = np.zeros(3, dtype='3int8, float32, (2,3)float64')
print xz

np.disp('abcd')
print x['bar']
print y
uz = np.union1d(x['bar'],y)
print uz

az= all([1,2,3,np.Inf])

print az
print all([])

xz1 = np.zeros(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})
print xz1
print xz1.dtype.fields['col1'][2]
'''
for k,v inzlable(v) :
        if inspect.isclass(v) :
            continue
        print k
'''