# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:07:23 2016

@author: 06411
"""
import pandas as pd
import numpy as np

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
           ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
           
tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

s = pd.Series(np.random.randn(8), index=index)
print(s)

print(s['bar'])
print(s['bar','one'])
print("==============================================================")

print(index)
print("==============================================================")
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
print(df)
print(df['bar'])
print(df['bar','one'])
print(df['bar']['one'])



tuples = [(1, u'red'), (1, u'blue'), (2, u'red'), (2, u'blue')]
mi = pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
print(mi)

arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
mi1 = pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
print(mi1)


numbers = [0, 1, 2]
colors = [u'green', u'purple']
mi2 = pd.MultiIndex.from_product([numbers, colors],names=['number', 'color'])
print(mi2)
print(mi2.names, type(mi2.names))
print(mi2.labels, type(mi2.labels))
print(mi2.levels, type(mi2.levels))

midx = pd.MultiIndex.from_product([list(range(3)),['a','b','c'],pd.date_range('20130101',periods=3)],names=['numbers','letters','dates'])
print(midx)
print(midx.levels[0])
print(midx.levels[1])
print(midx.levels[2])
print(midx.labels[0])
print(midx.labels[1])
print(midx.labels[2])
print(midx.names, type(midx.names))
print(midx.names.index('letters'))
print(midx.names.index('dates'))
print(midx.get_level_values(0))
print(midx.get_level_values(1))
print(midx.get_level_values(2))

print(midx.levels[0])

idx1 = pd.Index([1, 2, 3, 4])
idx2 = pd.Index([3, 4, 5, 6])
print(idx1.difference(idx2))
print(idx1, idx2)
idx3 = pd.Int64Index([1, 2], dtype='int64')
print(idx3)

idx4 = pd.Index(['a', 'b','c'])
print(idx4)

idx5 = pd.Index(pd.date_range('20130101',periods=3)) 
print(idx5)