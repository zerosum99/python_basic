# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:47:54 2016

@author: 06411
"""

import numpy as np
import numpy.linalg as lin



va = np.array([[1, 0]])
vb = np.array([[4, 1]])
vc = np.array([[4],[1]])
print(np.vdot(va,vb))
print(np.vdot(va,vc))
print(np.dot(va,vc))
print(np.inner(va,vb))
print("===================")
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
print(a.ndim, a.shape)
print(b.ndim, b.shape)
print(np.dot(a, b))
print(a[0])
print(b[0])
print(np.dot(a[0], b[0]))
print(np.dot(a[1], b[1]))
print(np.inner(a,b))
print("===================")

a = np.array([[1, 1], [1, 1]])
b = np.array([[4, 1,2], [2, 2,2]])
print(np.dot(a, b),np.dot(a,b).shape)
print(a.ndim, b.ndim)
print(a.shape, b.shape)