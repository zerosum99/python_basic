# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:54:30 2016

@author: 06411
"""

import numpy as np 
#ndarray 생성
x = np.arange(5.0)

#첫번째 원소 이동
y = x[0]
z = x[:1]

print(y)
print(z)

print(y is z)
print(y == z)

print(z.view())
y = 999
print(y)
print(x)
z[0] = 999

print(z)
print(x)

x = np.arange(5.0)
print(" ============   1d slicing =============")
s1 = slice(0,1)
print(x[[0,1]])
print(x[0:1])
print(x[s1])
print(" ============   1d indexing =============")
print(x[0])
print(" ============   2d slicing =============")
npx = np.array(np.arange(16).reshape(4,4))
print(npx)

print(npx[[1,2]])
sl = slice(0,2)
print(sl)
print(npx[sl])
print(npx[[1,2], 0:2])

print(npx[[1,2], [0,1]])
print(npx[1:3, 0:2])

print(" ============   2d indexing =============")
print(npx[0][1])

x=np.array([[1.0,2.0,3.0,4.0,5.0]])
print(x.shape, x.ndim)


x = np.array([[1.0,2.0],[3.0,4.0]])
y = np.array([[5.0,6.0],[7.0,8.0]])
z = np.concatenate((x,y),axis = 0)
print(z)
print(z.ndim, z.shape)

z = np.concatenate((x,y),axis = 1)
print(z)
print(z.ndim, z.shape)

z = np.vstack((x,y)) #  행기반 :concatenate((x,y),axis = 0)
print("vstack ", z)
z = np.hstack((x,y)) #  열 기반 : concatenate((x,y),axis = 1)
print("hstack ",z)




