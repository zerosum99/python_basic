# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 13:32:27 2016

@author: 06411
"""
import pandas as pd
import numpy as np
import math

obj = pd.Series([4,-7,5,3]) 

print(obj.index)
print(obj.values)

obj.index = ['a','b','c','d']
print(obj.index)
print(obj.values)

obj['a'] = 100
print(type(obj.values),obj.values)
print("===============================")
print(type(obj.blocks), obj.blocks)
print(type(obj.blocks['int64']),obj.blocks['int64'])
print(obj.dtype, obj.ftype)

print(type(obj.ix['a']),obj.ix['a'])
print(type(obj['a']),obj['a'])
print(type(obj.loc['a':'c']),obj.loc['a':'c'])
print(obj.loc[obj>5])
#obj.values = pd.Series([99,99,99,99]).values  #AttributeError: can't set attribute

obj1 = pd.Series([1,2,3,4],name="test") 
print(obj1.blocks)
print(obj1.blocks['int64'].index)
print(obj1.blocks['int64'].values)
print(obj1.blocks['int64'].name)
print(obj1.blocks['int64'].dtype)

obj1.index = ['a','b','c','d']
print(obj1.at['a'])
print(obj1.iat[0])

print(obj.iloc[0:3],obj.loc['a':'c'])

print(type(obj1.ix['a']),obj1.ix['a'] == 1)

obj2 = pd.Series([1,2,3,4])
obj3 = pd.Series([5,6,7,8])
print(obj2+obj3)
print(obj2-obj3)
print(obj2*obj3)
print(obj2/obj3)
print(obj2//obj3)
print(obj2%obj3)
obj4 = pd.Series(index=[0,1,2,3])

print(obj4)
print(obj2.add(obj4,fill_value=0))
obj2.astype(dtype=np.int64)
print(obj2)
print(obj2.add(obj4))
obj4[0] = 'na'
print(obj4,obj4.all())

obj4 = pd.Series(index=[0,1,2,3])
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data,type(data.values))
print(data.append(obj4))
obj5 = pd.Series([5,6,7,8],index=[5,6,7,8])
print(data.append(obj5,verify_integrity=True))

print(data.keys())
print(data.values)
for k,v in data.iteritems() :
    print (k,v),
print()
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data.sum(), data.sum()/len(data))
print(" average ",data.mean())
print(" median ",data.median())
print(" var ",data.var())

print(" standard deviation ",data.std())
print("      ",math.sqrt(data.var()))


long_series = pd.Series(np.random.randn(15))
print(long_series.head())
print(long_series.tail())
print(long_series.head(n=7))

print(pd.Series([True]).bool())
print(pd.Series([False]).bool())


data = pd.Series([0.25, 0.5, 0.75, 1.0])
print((data>0.5).all())
print((data>0.5).any())

obj_emp = pd.Series()
print(obj_emp.empty)

print(pd.DataFrame(columns=list('ABC')).empty)

print((data == data).all())
print((data+data != data).all())

print((data+data).equals(data*2))
print((data+data) == (data*2))
print(((data+data) == (data*2)).all())



series = pd.Series(np.random.randn(500))

series[20:500] = np.nan
series[10:20]  = 5
print(series)
print(series.nunique())

print(series.describe())
print(series.describe(percentiles=[.05, .25, .75, .95]))

s = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
print(s.describe())
print(s.unique())

sn = pd.Series([1,2,3,4,'a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
print(sn.describe(include=['object']))
print(sn.describe(include=['number']))
print(sn.unique())

obj = pd.Series([1,2,3,4])
print(obj.min())
print(obj.max())
print(obj.idxmin())
print(obj.idxmax())


data = np.random.randint(0, 7, size=50)
sv = pd.Series(data)

print(sv.value_counts())
print(sv.mode())

obj = pd.Series([1,2,3,4])
obj5 = obj * -1
print(obj5)
print(obj5.abs())

print(obj.replace(4,99))
print(obj)
print(obj.replace(4,99, inplace=True))
print(obj)

obj6 = pd.Series([4,4,4,4])
print(obj6.replace(4,99, inplace=True))
print(obj6)
print(obj6[:1].replace(99,4,inplace=True))
print(obj6)
obj7 = pd.Series([4,4,4,4])
print(obj7.set_value(1,999))
print(obj7)
print(obj7.sort_values(inplace=True))
print(obj7)

print(obj7.reindex([0,2,3,1]))
obj7.index = [0,1,2,3]
print(obj7)

obj8 = pd.Series([100,9,7,99])
print(obj8.sort())