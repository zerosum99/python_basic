# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:17:45 2016

@author: 06411
"""

def f(a):
    print "function class object ",id(f)
    def g(b, c, d, e):
        print(a, b, c, d, e)
    return g
    

print " function instance ", id(f(1))
 
f1 = f(1)
f1(2,3,4,5)


def f1(a):
    def g1(b):
        def h1(c, d, e):
            print(a, b, c, d, e)
        return h1
    return g1
 
f1(1)(2)(3,4,5)


from functools import partial
 
def f2(a, b, c, d):
    print(a, b, c, d)
 
print partial(f2,1,2,3)
g2 = partial(f2, 1, 2, 3)
g2(4)


def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(5))