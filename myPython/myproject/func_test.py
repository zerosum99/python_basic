# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:14:02 2015

@author: 06411
"""

def swap(a,b) :
   x = a[:]
   a[:] = b[:]
   b[:] = x[:]
            

 
func_var = swap   
a = [1]
b = [2]
#print(swap(a,b))
print(func_var(a,b))
print(a,b)

print(" 1 ",id(swap(a,b)))

print(" 2 ",id(swap(a,b)))

