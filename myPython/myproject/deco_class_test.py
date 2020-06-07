# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:07:02 2016

@author: 06411
"""

#테코레이터 클래스 정의하고 생성자에 함수 전달

class decoratorWithoutArguments(object):
    def __init__(self, f):
        print ("Inside __init__()")
        self.f = f

 #호출하는 곳에 내부함수 처리 로직 처리

    def __call__(self, *args):
        print( "Inside __call__()")
        self.f(*args)
        print( "After self.f(*args)")




#데코레이터 정의 및 전달함수 정의

@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print( 'sayHello arguments:', a1, a2, a3, a4)





print ("Preparing to call sayHello()")

sayHello("say", "hello", "argument", "list")

print ("After first sayHello() call")

sayHello("a", "different", "set of", "arguments")

print ("After second sayHello() call")




