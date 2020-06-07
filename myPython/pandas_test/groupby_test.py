# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:22:30 2016

@author: 06411
"""

import pandas as pd
import numpy as np

data = {'Platoon': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
       'Casualties': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}
df = pd.DataFrame(data)

print(df)
print('==================================================')
print(df.groupby("Platoon").describe())      # <pandas.core.groupby.DataFrameGroupBy object at 0x0F2C6190>

print(df.groupby("Platoon")['Casualties'])  # <pandas.core.groupby.SeriesGroupBy object at 0x0F2C7870>


print(df.groupby('Platoon')['Casualties'].apply(lambda x:pd.rolling_mean(x, 2)))
print('==================================================')
print(df['Casualties'].groupby(df["Platoon"])) 
print(df['Casualties'].groupby(df["Platoon"]).describe()) 
    
print(df.groupby('Platoon')['Casualties'].apply(sum))
print(df.groupby('Platoon')['Casualties'].apply(np.count_nonzero))
print(df.groupby('Platoon')['Casualties'].apply(np.mean))
print(df.groupby('Platoon')['Casualties'].apply(np.std))
print(df.groupby('Platoon')['Casualties'].apply(np.var))
print('==================================================')
print(df['Casualties'].groupby(df['Platoon']).apply(sum))
print(df['Casualties'].groupby(df['Platoon']).apply(np.count_nonzero))
print(df['Casualties'].groupby(df['Platoon']).apply(np.mean))
print(df['Casualties'].groupby(df['Platoon']).apply(np.std))
print(df['Casualties'].groupby(df['Platoon']).apply(np.var))

'''

print(df.index)
print(df.columns)
print(df.blocks)

def col_sum(df,col1, col2) :
    camp = ''
    col ={}
    sum = {}
    count = {}
    for x in range(16) :
        
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
print(col_sum(df,'Platoon' ,'Casualties' ))

'''