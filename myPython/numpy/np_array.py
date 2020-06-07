# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:00:25 2016

@author: 06411
"""

import numpy

print dir(numpy.array)

a = numpy.array([1,2,3])
#print " a ",dir(a)
print a.shape
print a.ndim
print a.dtype
print a.size
print a.itemsize
print repr(a.data.__str__())

print "===== a.dtype =======    "
for k,v in numpy.dtype.__dict__.items():
     if callable(v) :
         pass
     else :
         print k
print "===== a.dtype =======    "
b = numpy.dtype(numpy.int16)
print b.char
print b.shape
print b.num
print b.names
print b.hasobject