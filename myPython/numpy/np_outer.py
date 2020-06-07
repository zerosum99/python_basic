# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:28:36 2016

@author: 06411
"""

import numpy as np




a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
print(np.matmul(a, b))
print(np.dot(a,b))
print(np.inner(a,b))
a = [[1, 0,3], [0, 1,3]]
b = [[4, 1], [2, 2],[3,3]]
print(np.matmul(a, b))
print(np.dot(a,b))
# print(np.inner(a,b)) 동일하지 않아서 오류처리


a = [[1, 0], [0, 1]]
b = [1, 2]
print(np.matmul(a, b))
print(np.matmul(b, a))
a = [[1, 0], [0, 1]]
b = [[4, 1,1], [2, 2,3]]
print(np.matmul(a, b))
#print(np.matmul(b, a))

a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
ts = np.tensordot(a,b,axes=0)
print(ts)
print(ts.ndim, ts.shape)
print(np.tensordot(a,b,axes=1))
print(np.dot(a,b))
print(np.tensordot(a,b,axes=2))
print(np.dot([1,0,0,1],[4,1,2,2]))

print(ts[0])
print(ts[0][0])
print(ts[0][0][0])
print(ts[0][0][0][0])


from numpy import linalg as LA
i = np.array([[0, 1], [-1, 0]]) # matrix equiv. of the imaginary unit
print(LA.matrix_power(i, 3))  # should = -i

i = np.array([[2, 3], [4, 5]]) 
print(LA.matrix_power(i, 3))
s = np.dot(i,i)
print(np.dot(s,i))

print('=======================')
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
print(np.outer(a,b))
print(a.shape,b.shape,np.outer(a,b).shape)
print(np.cross(a,b))

a = np.array([[1,2,3]])
b = np.array([[4,5]])

print(np.outer(a,b))

a = np.array([[1,0]])
b = np.array([[4,1]])
print('=======================')
print(np.outer(a,b))
print(a.shape, b.shape,np.outer(a,b).shape)
rl = np.outer(np.ones((5,)), np.linspace(-2, 2, 5))

print(np.ones(5,))
print(np.linspace(-2,2,5))

print(rl)

x = np.array(['a', 'b', 'c'], dtype=object)
print(np.outer(x, [1, 2, 3]))
y = np.array([1,2,3], dtype=object)
print(np.outer(y, ['a', 'b', 'c']))

a = np.array([[2,3,4],[2,4,8],[3,6,9]])
print(np.linalg.det(a))

a = np.array([[1,2],[3,4]])
print(np.linalg.inv(a))