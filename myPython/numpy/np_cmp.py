# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:12:43 2016

@author: 06411
"""

import numpy as np

A = np.array([4, 7, 3, 4, 2, 8])
C = (A==4)
print C, type(C)

LT = (A < 5)
print LT, type(LT)

B = np.array([[142,56,189,65],
              [299,288,10,12],
              [55,142,17,18]])
print(B>=82)

b = B>82
c = b.astype(np.int)
print c

d = B[B>82]
print d

print "fffffffffffffff"
e0 = np.array([0,0,0,0])
e1= np.array([0,3,2,1])
f = B[(e0,e1)]
print f

print " multi index "
e0 = np.array([0,0,1,1])
e1= np.array([0,3,2,1])
f = B[(e0,e1)]
print f

A = np.array([3,4,6,10,24,89,45,43,46,99,100])
#3으로 나눠지지 않는 수 추출
print (A%3 != 0)
g = A[A%3 !=0]
print g

Z = np.array([[142,56,0,65],
              [0,288,10,12],
              [55,142,0,18]])
            
z = Z[Z.nonzero()]
print Z.nonzero()
print np.transpose(Z.nonzero())
print z
print np.transpose(np.transpose(Z.nonzero()))
print np.count_nonzero(Z)
print np.flatnonzero(Z)

is_prime = np.ones((100,), dtype=bool)
print is_prime
is_prime[:2] = 0
print is_prime
nmax = int(np.sqrt(len(is_prime)))
print nmax
for i in range(2, nmax):
    is_prime[2*i::i] = False
print is_prime
print(np.nonzero(is_prime))


x = np.array([1,5,2])
y = np.array([7,4,1])
print x + y
print x * y
print x - y
print x / y
print x % y

bb = np.array([1,2,3])
cc = np.array([-7,8,9])
print np.dot(bb,cc),type(np.dot(bb,cc))

xa = np.array( ((2,3), (3, 5)) )
ya = np.array( ((1,2), (5, -1)) )
print xa*ya

xm = np.matrix( ((2,3), (3, 5)) ) 
ym = np.matrix( ((1,2), (5, -1)) )
print xm*ym
print type(xm)
print np.dot(xm,ym), type(np.dot(xm,ym))

print np.mat(xa) * xm
print np.asmatrix(xa) * xm


persons = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
print "  persons shape ", persons.shape
Price_per_100_g = np.array([2.98,3.90,1.99])
print Price_per_100_g.shape
Price_in_Cent = np.dot(persons,Price_per_100_g)
print Price_in_Cent, type(Price_in_Cent,)
Price_in_Euro = Price_in_Cent / np.array([100,100,100,100])
print Price_in_Euro


xs = np.array( ((2,3), (3, 5)) ) 
ys = np.array( ((1,2), (5, -1)) )
print np.dot(xs,ys), type(np.dot(xs,ys))


xm = np.matrix( ((2,3), (3, 5)) ) 
ym = np.matrix( ((1,2), (5, -1)) )

print xm-ym
print xm+ym

print 5 *xm

x = np.array([0,0,1])
y = np.array([0,1,0])

print np.cross(x,y)
print np.cross(y,x)
