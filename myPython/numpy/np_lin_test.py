# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:44:24 2016

@author: 06411
"""

import numpy as np

a1 = np.array( [1, 2, 3] ) #크기 (3,)인 1차원 배열
a2 = np.array( [ [1, 2, 3] ] ) #크기 (1,3)인 2차원 배열 (행벡터)
a3 = np.array( [ [1], [2], [3] ] ) #크기 (3,1)인 2차원 배열 (열벡터)

print(a1)
print(a1.ndim, a1.shape)
print(a2)
print(a2.ndim, a2.shape)
print(a3)
print(a3.ndim, a3.shape)

print(a1 * a1)
print(np.multiply(a1,a1))
print(np.dot(a1,a1.T))
print(a1.dot(a1.T))

print(a2 * a2)
print(np.multiply(a2,a2))
print(np.dot(a2,a2.T))
print(a2.dot(a2.T))

print(a3 * a3)
print(np.multiply(a3,a3))
print(np.dot(a3,a3.T))
print(a3.dot(a3.T))


m1 = np.matrix([1,2,3,4])
print(m1, type(m1))
print(m1.ndim, m1.shape)

a1 = np.array([1,2,3,4])
print(a1, type(a1))
print(a1.ndim, a1.shape)

print(m1*m1.T)
print(m1.dot(m1.T))
print(np.multiply(m1,m1))

print(a1*a1.T)
print(a1.dot(a1.T))
print(np.multiply(a1,a1))


a = np.array([[1, 4], [5, 6]])
b = np.array([[4, 1], [2, 2]])
print(a * b)


d = np.matrix([4,5])
e = np.matrix([3,8])

f = d + e
print(f)

d = np.matrix([1,2])
e = np.matrix([2,1])
g = d - e
print(g)

d = np.matrix([1,2])
i = 3 * d 
print(i)

import math
x = np.matrix([1,2])
print(type(x), x.shape, x[0][:])
print(np.array(x)[0])
mag = lambda x: math.sqrt(sum(i**2 for i in x))
print(mag(np.array(x)[0]))

print(np.linalg.norm(x))


d = np.matrix([4,5])

j= d*d.T
print(j)
print(np.dot(d,d.T))

d = np.matrix([4,5])
e = np.matrix([3,8])

print(np.cross(d,e))

d = np.matrix([4,5,4])
e = np.matrix([3,8,2])
print(np.cross(d,e))

print(d)
print(d[0])

print(d[0,1])






