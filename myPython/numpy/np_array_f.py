# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:26:26 2016

@author: 06411
"""

import numpy as np

A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))

print(A.ravel())
print(A.ravel(order="A"))
print(A.ravel(order="F"))
print(A.ravel(order="A"))
print(A.ravel(order="K"))

X = np.array(range(24))
Y = X.reshape((3,4,2))
print Y


x = np.array([11,22])
y = np.array([18,7,6])
z = np.array([1,3,5])
c = np.concatenate((x,y,z))
print(c)

x = np.array(range(12))
x = x.reshape((2,3,2))
y = np.array(range(100,112))
y = y.reshape((2,3,2))
z = np.concatenate((x,y))

print(z)

x = np.array([2,5,18,14,4])
y = x[:, np.newaxis]
print(y)
x = np.arange(6)
y = x.reshape(2,3)
print y[:,np.newaxis]

A = np.array([3, 4, 5])
B = np.array([1,9,0])
print(np.row_stack((A, B)))
print(np.column_stack((A, B)))
print np.shape(A)

A = np.array([[3, 4, 5],
              [1, 9, 0],
              [4, 6, 8]])
print A.shape
print np.column_stack((A, A)).shape
print np.row_stack((A, A)).shape