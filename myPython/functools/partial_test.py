# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:57:23 2016

@author: 06411
"""

def add(x, y):
    return x + y

from functools import partial

add5_partial = partial(add, 5)
print type(add5_partial)
print add5_partial(10) # 15

def part(x) :
    def add(y) :
        return x+ y
    return add

part_1 = part(5)
print part_1(10) 
    
add5_lambda = lambda x: add(x, 5)
print add5_lambda(10) # 15


class Foo(object):
    x = 9
    def __init__(self,x):
        self.x = x    # x는 로컬변수 처리
 
    def bar(self,y):
        return self.x + y
        
foo = Foo(5)
print foo.x
print foo.bar(4) == 9
print foo.bar(0) == 9   
print Foo.bar(foo,0)


def bar1(self,y):
    return self.x + y   #x는 self가 class 일 경우 클로벌 변수 사용
 
class Foo1(object):
    x = 9
    def __init__(self,x):
        self.x = x
    bar = bar1    

foo1 = Foo1(5)
 
print bar1(foo1,4) == 9
print bar1(Foo1,0) == 9
print foo1.bar(0)
print foo1.bar(4)