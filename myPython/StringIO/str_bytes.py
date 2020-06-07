# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 12:02:07 2016

@author: 06411
"""
print(' start ')
for i in dir(bytes) :
    if i in dir(str) :
        pass
    else :
        print(i)
else :
    print(' end ')
    

print(' start ')
for i in dir(str) :
    if i in dir(object) :
        pass
    else :
        print(i)
else :
    print(' end ')
    
print(' start unicode ')
for i in dir(unicode) :
    if i in dir(str) :
        pass
    else :
        print(i)
else :
    print(' end ')
    
    
print(' start string ')
import string
for i in dir(string) :
    if i in dir(str) :
        pass
    else :
        print(i)
else :
    print(' end ')
    
print(' start bytearray')

for i in dir(bytearray) :
    if i in dir(str) :
        pass
    else :
        print(i)
else :
    print(' end ')