# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 13:03:01 2016

@author: 06411
"""

from collections import OrderedDict
from collections import defaultdict
from collections import deque

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

print 'ordered dict : ', od
print ' dict        : ', d




def default_factory():
    return 'default value'

d = defaultdict(default_factory, foo='bar')
print 'd:', d
print 'foo =>', d['foo']
print 'bar =>', d['bar']

dl = defaultdict(list, foo=[1,2,3])
print 'dl : ',dl



d = deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d

print OrderedDict.__module__

print __name__
print default_factory.__module__