# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:38:24 2016

@author: 06411
"""

import numpy as np
import math

a = np.array(np.arange(4))

print(np.dot(a,a))
print(np.inner(a,a))
print(np.vdot(a,a))

a = np.array(np.arange(4).reshape(2,2))
b = np.matrix(a)
print(b*b)
print(np.matmul(a,a))
print(np.dot(a,a))
print(np.tensordot(a,a,axes=1))
print(np.inner(a,a))
print(np.tensordot(a,a,axes=(-1,-1)))
print(np.vdot(a,a))

print(np.array(np.arange(3*5)))
print(np.array(np.arange(3*5))[::-1])
a = np.array(np.arange(3*5)).reshape(3,5)
b = np.array(np.arange(3*5))[::-1].reshape(5,3)

print(np.dot(a, b)[2,1])


s = 10
v = [1,2,3]
m = np.array([[1,2,3],[4,5,6]])
print(s, type(s))
print(v, type(v))
print(m, type(m))

print(np.linalg.norm(v))
print(math.sqrt(v[0]**2+v[1]**2+v[2]**2))

def add(u, v):
    return [ u[i]+v[i] for i in range(len(u)) ]

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))
    
def normalize(v):
    vmag = magnitude(v)
    return [ v[i]/vmag  for i in range(len(v)) ]

l = [1, 1, 1]
v = [0, 0, 0]
h = normalize(add(l, v))
print(magnitude(add(l,v)))
print h

a=[2,3]
b=[5,6]
print(np.cross(a,b))
print(np.dot(a,b))
print(np.multiply(a,b))

a=[1,2,3]
b=[4,5,6]
print(np.dot(a,b))
print(np.cross(a,b))

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a+b)
print(a-b)
print(a*b)
print(np.dot(a,b))
print(np.multiply(a,b))

a = np.array([[1,2],[3,4]])
print(a.T)
print(np.transpose(a))


a = np.array(np.arange(12).reshape(2,3,2))
b = np.array([[5,6],[7,8]])

print(a.shape)
print(np.inner(a,b))

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.inner(a,b))

a =  np.array([[3,1],[2,2]])
print(np.linalg.det(a))

a =  np.array([[3,1,3],[2,2,3],[1,1,1]])
print(np.linalg.det(a))
s,md = np.linalg.slogdet(a)
print(np.linalg.slogdet(a))
print(s * np.exp(md))
print(a[1:,1:])
print(np.linalg.det(a[1:,1:]))
m11 = np.linalg.det(a[1:,1:])
print(a[1:,(0,2)])
print(np.linalg.det(a[1:,(0,2)]))
m12 = np.linalg.det(a[1:,(0,2)])
print(a[1:,(0,1)])
print(np.linalg.det(a[1:,(0,1)]))
m13 = np.linalg.det(a[1:,(0,1)])
print(a[0,0]*m11-a[0,1]*m12+a[0,2] *m13)

print(np.linalg.inv(a))


a = np.array([1,0])
b = np.array([4,1])
print(a.shape, b.shape)
print(np.outer(a,b))

a = np.array([[1,0],[1,0]])
b = np.array([[4,1],[4,1]])
print(np.outer(a,b))

a1 = np.array([[1,0,3]])
b1 = np.array([[4,1,3]])
print(a1.shape, b1.shape)
print(np.inner(a1,b1))

a = np.array([[1,0]])
b = np.array([[4,1]])
print(a.shape, b.shape)
print(np.outer(a,b))
print(np.dot(a.T,b))

a = np.array([[1,0],[1,0]])
b = np.array([[4,1],[4,1]])
print(np.trace(a))
print(np.trace(b))


a = np.array([[1,0],[0,1]])
b = np.array([[4,1],[2,2]])
print(a.shape, b.shape)
print(np.inner(a,b))


a = np.array([[1,0],[0,1]])
b = np.array([[4,1],[2,2]])
print(np.cross(a,b))

a = np.arange(8).reshape((2,2,2))
print(a)
print(np.trace(a))

b = np.array([[[0, 1],[2, 3]], [[7,8], [6, 7]]])
print(b)
print(np.trace(b))

a = np.random.randn(1,2)
print(a)
print(np.linalg.norm(a))
q, r = np.linalg.qr(a)
print(q)
print(r)
q2 = q*q
r2 = r * r
aa = np.sqrt(q2+r2)
print(aa)

print("=================================")
a = np.array([[1,0]])
b = np.array([[4,1]])

q,r = np.linalg.qr(a)
print(q)
print(r)
aa1 = np.sqrt(np.dot(q,r))
print(aa1)
aa2 = np.linalg.norm(a)
print(aa2)

a = np.array([[1,0],[0,1]])
b = np.array([[4,1],[3,2]])
print(np.dot(b,a))
print(np.dot(a,b))

v = [[ 10,20],[10,20]]
print(np.linalg.eigvals(v))

v = [[ 2,1],[1,2]]
print(np.linalg.inv(v))

