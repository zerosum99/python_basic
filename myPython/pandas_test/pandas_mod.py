# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:05:56 2016

@author: 06411
"""

import pandas as pd
import inspect as ins

print(" Pandas Class list ")   
for k,v in pd.__dict__.items() :
    if ins.isclass(v) :
        print(k,v)
print(" DataFrame Method list ")       
for k,v in pd.__dict__.items() :       
    if k == "DataFrame" :
        for kk,vv in v.__dict__.items() :
            if ins.ismethod(vv)  or  \
               ins.isroutine(vv) :
                print(kk,vv)
        
print(" DataFrame variable list ")       
for k,v in pd.DataFrame.__dict__.items() :       
       
      if ins.ismethod(v):
          continue
      elif ins.isfunction(v) :
          continue
      else :
          print(k)
    
print(" DataFrame instance method list ")       
for k,v in pd.DataFrame.__dict__.items() :       
       
      if ins.isroutine(v)     :
          if ins.ismethod(v)  or \
             ins.isfunction(v) :
              continue
          else :
              print(k)
      else :
          continue  