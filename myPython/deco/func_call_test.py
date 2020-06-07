# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:48:22 2016

@author: 06411
"""

#외부함수 정의
def out_f(x,y) :
    return x+y
    
# 외부함수 호출
def call_out_f() :
    return out_f(5,5)

print ' call global function out_f ', call_out_f()



# 내장 함수 호출    
def call_builtin_f():
    return sum((5,6))


print ' call builtin function sum ', call_builtin_f()
