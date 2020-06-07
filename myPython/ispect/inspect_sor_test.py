# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:15:25 2016

@author: 06411
"""

import inspect

def sum(x,y) :
    return x+y
    
def add(x,y) :
    return x + y

def func_c(x) :
    def add(y) :
        return x + y
    return add
print(" function sum variable ")  
print("tuple of names of arguments and local variables")
print(sum.func_code.co_varnames)
print("dict of names of arguments ")
print(inspect.getcallargs(sum,5,5))
print(" function sum code ")  
print(sum.func_code.co_code)
print(inspect.getsource(sum))
print(inspect.getsourcefile(sum))

f_add = func_c(5)
#print(inspect.stack())
print(" function func_c ")  
print(f_add(6))
print(inspect.getsource(func_c))
print(inspect.getcallargs(func_c,5))
print(inspect.getcallargs(f_add,6))


def add_ar(*args, **kagrs) :
    sum = 0
    print(locals())
    for i in args :
        sum += i
    for k,v in kagrs.items():
        sum += v
   
    return sum
    
print(add_ar(1,x=1,y=1))
