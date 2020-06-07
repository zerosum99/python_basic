# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:18:49 2016

@author: 06411
"""
_functions = {}
def register(func) :
    global _functions
    _functions[func.__name__] = func
    return func

def wrapper(func,*args, **kargs) :
    return func(*args, **kargs) 

def deco_f(func) :
    print "deco_f ", func.__name__
    return func
    
 
    
@register    
@deco_f
def add(x,y) :
    return x+y
    
print add(5,5)
print _functions

print " process order "
add = deco_f(register(add))
print add(5,5)
print _functions

deco = deco_f(wrapper)
print deco(add,5,5)
print _functions


def out_f(x,y) :
    return x+y
    
def call_out_f() :
    return out_f(5,5)
    
def call_builtin_f():
    return sum((5,6))


print ' call global function out_f ', call_out_f()
print ' call builtin function sum ', call_builtin_f()

def func_para_f(func) :
    return func(5,6)
    
print ' func para ', func_para_f(add)

def outer_f(x,y) :
    def inner_f(x,y) :
        return x+y
    return inner_f(x,y)
    
print outer_f(5,5)

def closure_out(x,y) :
    
    def closure_in() :
        return x + y
        
    return closure_in
    
clo = closure_out(5,5)
print clo()
print clo.func_closure
print clo.__dict__
print clo.func_closure[0].cell_contents



print " func_para_all"
def func_para_all(func,*args, **kargs) :
    return func(*args, **kargs)
    
print func_para_all(add,5,5)

print " func_para_all"
def func_all(func) :
    def wrapper(*args, **kargs) :
        return func(*args, **kargs)
        
    return wrapper
    
fa = func_all(add)
print fa(5,5)
print fa.func_closure[0].cell_contents

print " func chain "
def A(func) :
    return func
    
def B(func) :
    return func
    
def C(func) :
    return func
    
def exec_f(x,y) :
    return x+y
  
print A(B(C(exec_f)))  == exec_f  
  
print A(B(C(exec_f)))(5,6)

from functools import wraps
def func_para(func) :
    print func.__doc__
    print func.__name__
    @wraps(func)
    def wrapper(*args, **kargs) :
        print " wrapper ",func.__doc__
        print " wrapper ",func.__name__
        return func(*args, **kargs)
    return wrapper
@func_para  
def tr() :
    """ doc  """
    print(" tranfer func ")
    
#func_para(tr)
tr()
print "xxxx ", tr.__doc__, tr.__name__
