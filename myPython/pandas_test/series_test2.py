# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:19:54 2016

@author: 06411
"""

import pandas as pd
import numpy as np

obj = pd.Series([1,2,3,4])
obj1 = pd.Series([5,6,7,8])
obj2 = pd.Series([5,6,7,8,9])

obj3 = obj.add(obj1)
print("add",obj3)
print("radd",obj.radd(obj1))
print(obj.add(obj2))
print(obj)
print("sub",obj.sub(obj1))
print("rsub",obj.rsub(obj1))
print("mul",obj.mul(obj1))
print("rmul",obj.rmul(obj1))
print("div",obj.div(obj1))
print("rdiv",obj.rdiv(obj1))
print("floordiv", obj.floordiv(obj1))
print("rfloordiv", obj.rfloordiv(obj1))
print("truediv",obj.truediv(obj1))
print("rtruediv",obj.rtruediv(obj1))
print("divide",obj.divide(obj2, fill_value=0.0))
print("mod",obj.mod(obj1, fill_value=0.0))
print("rmod",obj.rmod(obj1, fill_value=0.0))

for k,v in pd.Series.__dict__.items() :
    for kk,vv in pd.DataFrame.__dict__.items() :
        if k == kk :
            print(k)