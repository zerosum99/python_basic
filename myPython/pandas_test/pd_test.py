# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:11:41 2016

@author: 06411
"""


import pandas as pd
import inspect as ins

for k,v in pd.__dict__.items() :
    if ins.isclass(v) and k == 'Series' :
        print(" class : ", k)
        count = 0
        for kk,vv in v.__dict__.items() :
            if ins.isroutine(vv) :
                count += 1
                print("method : ",count , kk)
        
        