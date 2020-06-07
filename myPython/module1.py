# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:22:29 2015

@author: 06411
"""

from functools import *

def intersect(*ar) :
    "교집합"
    
    return reduce(__intersectSC, ar)
    
def __intersectSC(listX, listY) :
    setList=[]
    for x in listX :
        if x in listY :
            setList.append(x)
    return setList
    
if __name__ == '__main__' :
    print " call module "
else :
    print " call import "