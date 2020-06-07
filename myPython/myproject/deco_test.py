# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:30:05 2015

@author: 06411
"""
import time
 
def checkTime(func):
    def newFunc(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print end - start
    return newFunc

@checkTime
def aFunc(maxValue):
    for i in range(1,maxValue+1):
        print i

@checkTime
def bFunc():
    print "This is Function-B"

@checkTime
def cFunc(start, end):
    for i in range(start, end+1):
        print i
        
v = checkTime(aFunc)
print(type(v))
print(v)
v(5)


