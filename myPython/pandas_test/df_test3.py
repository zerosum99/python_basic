# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:02:10 2016

@author: 06411
"""

import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
print(df)

bins = [0, 25, 50, 75, 100]

group_names = ['Low', 'Okay', 'Good', 'Great']
categories = pd.cut(df['postTestScore'], bins, labels=group_names)
print(categories)
df['categories'] = pd.cut(df['postTestScore'], bins, labels=group_names)
print(categories)

print(pd.value_counts(df['categories']))
print(df)

print(pd.DataFrame.__class__.__name__)

data1 = {'a':1,'b':2}
sr = pd.Series(data1)
print(sr)
print(sr.values)
print(sr.index.__dict__['_data'])
