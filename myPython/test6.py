# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:56:24 2015

@author: 06411
"""

def divide(a, b) :
    return a/b
    
try :
    c = divide(5, 'string')
except ZeroDivisionError:
    print ' zero devide '
except TypeError :
    print ' Type error '
except :
    print ' do not know '
    
    