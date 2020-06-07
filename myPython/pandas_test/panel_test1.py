# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:36:28 2016

@author: 06411
"""

import pandas as pd
import numpy as np

pn = pd.Panel(np.random.rand(4,3,2))
print(pn)
print("items", pn.items)
print("major ", pn.major_axis)
print("minor ", pn.minor_axis)

wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
major_axis=pd.date_range('1/1/2000', periods=5),minor_axis=['A', 'B', 'C', 'D'])
print('=================')
print(wp)
print(wp['Item1'])
print(wp['Item2'])

print(wp.major_axis[2])
print(wp.major_xs(wp.major_axis[2]))

print(wp.minor_axis[1])
print(wp.minor_xs(wp.minor_axis[1]))
print(wp.minor_xs('B'))

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
         'Item2' : pd.DataFrame(np.random.randn(4, 2))}


wp1 = pd.Panel(data)
print(wp1)
print(wp1['Item1'])
print(wp1['Item2'])

xx = np.random.randn(1,1,1)
pn1 = pd.Panel(xx)
print(xx)
print(pn1)
print("items", pn1.items)
print("major ", pn1.major_axis)
print("minor ", pn1.minor_axis)
print('++++++++++++++++++++++++++++')
print("items", pn1[0])
print("major ", pn1.major_xs(pn1.major_axis[0]))
print("minor ", pn1.minor_xs(0))