# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:16:02 2015

@author: 06411
"""

# 변수에 할당없이  연산이 되는 경우 에러
# i = i + 1

def a(x,y) :
    print locals()
    print 'a x : ', id(x)
    print 'a y : ', id(y)
    #UnboundLocalError: local variable 'c' referenced before assignment
    c = 1
    #c = [0,1]
    print locals()
    def b(x,y) :
        print locals()
        print 'b x :', id(x)
        print 'b y : ', id(y)
       
        
        c =0
        c = c+ 1
        #c[0] = c[0] + 1
        
        
    b(x,y)
    #print ' c [0] : ', c[0]
        
a(1,2)