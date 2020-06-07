# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:59:10 2016

@author: 06411
"""
#고차 함수 정의
def addList8(list):
    return reduce(add8, list)
#일반함수 정의
def add8(*arg): 
    v = []
    for i in arg :
          v = v + i
    return v

#고차함수 실행
print addList8([[1, 2, 3],[4, 5],[6],[]])

print reduce(add8, [[1, 2, 3],[4, 5],[6],[]])


def addList7(list):
    return reduce(add, list)
    
def add(*arg): 
    x = 0
    for i in arg :
        x = x + i
    return x
    
print "addlist", addList7([1, 2, 3])

print "reduce ", reduce(add, [1, 2, 3])

#함수를 변수에 할당
func = add
print func

# 함수를 함수의 인자로 전달
def addplus(func,x,y) :
    return func(x,y)
    
print addplus(add,5,5)

# 함수를 함수의 리턴 결과로 전달

def addpass(func) :
    return func

print addpass(add)(5,5)

print addpass(lambda x,y: x+y)(5,5)

