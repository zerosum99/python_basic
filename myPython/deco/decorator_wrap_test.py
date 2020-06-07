# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:36:49 2016

@author: 06411
"""

def common_func(func) :
    
    def wrap_func() :
        return func()
    
    return wrap_func

@common_func
def r_func() :
    print " r func "
    
    
r_func()
        
        
def parent() :
    return object
    
class A(parent()) :
    pass

print A.mro()

class test1(object) :
    print " test1 "

print test1.mro()


class A(object) :
    bar = 100
    def foo(self) :
        print " self foo "
    @classmethod
    def cls_foo(cls) :
        print " cls foo "
    
class B(object) :
    bar = 0
    
class C(A,B) :
    xyz = 'abc'
    
print " super function ", super(C,C())

print C.mro()
print super(C,C()).__self__
print super(C,C()).bar
print super(B,B()).__self__
print super(B,B()).__self__.bar


print super(C)
#print super(C).foo  # 인스턴스 메소드는 오류
print super(C,C()).cls_foo
c = super(C)
print c

class D(C) :
    sup = super(C)
    
print D().sup
print D().sup.foo
print super(C,D()).foo
print D().sup.bar







