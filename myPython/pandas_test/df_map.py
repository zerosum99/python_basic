# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:24:54 2016

@author: 06411
"""

import pandas as pd
import numpy as np

data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'year': [2012, 2012, 2013, 2014, 2014], 
        'reports': [4, 24, 31, 2, 3],
        'coverage': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data) # index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(df)

capitalizer = lambda x: x.upper()
print(df['name'].apply(capitalizer))

print(df['name'].map(capitalizer))


df1 = df.drop('name', axis=1)
print(df1)

print(df1.applymap(np.sqrt))

def col_sum(df,col1='year', col2='coverage') :
    camp = ''
    col ={}
    sum = {}
    count = {}
    for x in range(5) :
        
        #칼럼 값 분류 기준
        if camp !=  df.loc[x,col1] :
            camp = df.loc[x,col1]
            if camp not in col.keys() :
                col[camp] = []
                
            if camp not in sum.keys() :   
                sum[df.loc[x,col1]] = 0
            if camp not in count.keys() :
                count[df.loc[x,col1]] = 0
            
         #칼럼별 분류   
      
        col[camp].append(df.loc[x,col2])
        sum[df.loc[x,col1]]+= df.loc[x,col2]
        count[df.loc[x,col1]] += 1
            
    return sum,count, col
print(col_sum(df1,'year' ,'coverage' ))


def times100(x):
    if type(x) is str:
        return x
    elif x:
        return 100 * x
    else:
        return
print(df.applymap(times100))


dfx = pd.DataFrame(np.arange(16).reshape(4,4))
print(dfx)

print(dfx.apply(sum))