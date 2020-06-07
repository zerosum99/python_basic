# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:39:41 2016

@author: 06411
"""

a = input(">")
print(a)

# 함수에서 클래스를 리턴해서 클래스를 만드는 법

def class_with_method(func):

    class klass: 

        pass

    # setattr(obj, name, value, /)

    #  setattr(x, 'y', v) is equivalent to ``x.y = v''

    setattr(klass, func.__name__, func)

    return klass

    

def say_foo(self): 

    print('foo')

    

Foo = class_with_method(say_foo)

print('Foo dict ', Foo.__dict__)

foo = Foo()

foo.say_foo()


#type  type(object_or_name, bases, dict)

#  type(object) -> the object's type

#  type(name, bases, dict) -> a new type




def __init__(self, x=None):

    self._x = x




def set_x(self, value):

    self.x = value




SubClass = type('SubClass', (object,), { '__init__':__init__,'set_x': set_x})

# (More methods can be put in SubClass, including __init__().)




print(SubClass.__dict__)

obj = SubClass()

obj.set_x(42)

print( obj.x ) # Prints 42

print (isinstance(obj, object) )



class BaseClass(object) :

    def __init__(self,x) :
        self.x = x

        

SubClass1 =  type('SubClass', (BaseClass,), { 'set_x': set_x})

obj1 = SubClass1(5)

print(obj1.x)
obj1.set_x(50)

print(obj1.x)




#'type' descendent as class factory (python)




class ChattyType(type):

    def __new__(cls, name, bases, dct):

        print( "Allocating memory for class", name)
        
        return type.__new__(cls, name, bases, dct)
    
    def __init__(cls, name, bases, dct):

        print ("Init'ing (configuring) class", name)
        print( cls.__dict__)
        super(ChattyType, cls).__init__(name, bases, dct)
        print( cls.__dict__)
 
        
print(" class processing ")
X = ChattyType('X',(),{'foo':lambda self:'foo'})

print(" instance processing")

print('XXXX', X.__dict__)
print(isinstance(X(), X))
print( X().foo())

Y = ChattyType('Y',(),{'bar':lambda self:'bar'})
print(" instance processing")

print(Y)
print(" YYYYYY ", Y.__dict__)
print(" mro ",Y.mro())
print(isinstance(Y(), Y))
print( Y().bar())
#(<class '__main__.X'>, 'foo')

