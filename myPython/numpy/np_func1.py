# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:16:25 2016

@author: 06411
"""

import numpy as np

a = np.arange(6)
b = np.arange(6).reshape(2,3)
a[5] = 100

print a
print b
print a[np.argmax(a)]


print np.argmax(b, axis=0)  # 열 처리
print np.argmax(b, axis=1)  # 행 처리


cvalues = [25.3, 24.8, 26.9, 23.9]
#섭씨 ndarray 생성
C = np.array(cvalues)
print(C)
F = C * 9 / 5 + 32
print(F)

#기존방식, 리스트 컴프리헨션도 loop문 실행

F = [ x*9/5 + 32 for x in cvalues] 
print(F)

l = range(1,10)
print type(l),l
nparr = np.arange(1,10,dtype=np.float_)
print type(nparr), nparr

print l.__getitem__(1)

arI = np.array([True,False,True,False,True,False,True,False,True,False])
print arI, arI.dtype
print nparr.__getitem__(1)
print nparr.__getitem__(arI)

print l.__setitem__(1,100),l
print nparr.__setitem__(1,100), nparr
print nparr.__setitem__(arI, 99), nparr


print nparr
s = open('arraystore.nd', 'w')
np.save(s,nparr)
s = open('arraystore.nd', 'r')
ndx = np.load(s)
print ndx
s.seek(0)
print s.read()



samples, spacing = np.linspace(1, 10, 10,retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=True, retstep=True)
print(spacing)
samples, spacing = np.linspace(1, 10, 20, endpoint=False, retstep=True)
print(spacing)

import time
size_of_vec = 10000

def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    print t1
    return time.time() - t1
def numpy_version():
    t2 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    print t2
    return time.time() - t2
    
t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2)
#print("Numpy is in this example " + str(t1/t2) + " faster!")

x = np.array(42)
print x, x.ndim


x = np.array([[42,22,12],[44,53,66]], order='F')
y = np.copy(x)
z = x.copy()
x[0,0] = 1001
print(x)
print(y)
print(z)
print x.flags

o = x
print id(o), id(x)
o = x.copy()
print id(o), id(x)
