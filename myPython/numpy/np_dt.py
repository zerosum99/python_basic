# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:50:30 2016

@author: 06411
"""

import numpy as np

f = np.float(1.0)
print f

f_ = np.float_(1.0)
print f_,f_.dtype.char, f_.itemsize
print f_.dtype.names, f_.dtype.name
print f_.dtype.shape
print f_.dtype.num
print f_.dtype.type
print f_.dtype.str
print f_.dtype.isbuiltin
print f_.dtype.byteorder
print f_.dtype.alignment
print f_.dtype.isalignedstruct
print f_.dtype.descr
print f_.dtype.hasobject
print f_.dtype.subdtype
print f_.dtype.base
print f_.dtype.kind
print f_.dtype.isnative
print f_.dtype.flags
print f_.dtype.fields
print f_.dtype.metadata

x = np.array([(1,2.,'Hello'), (2,3.,"World")], dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])

print str(x[0]['baz'].data)
print str(x[0]['foo'].data)

'''

itemsize
alignment
isalignedstruct
isbuiltin
descr
__doc__
hasobject
subdtype
base
byteorder
kind
isnative
flags
str
fields
metadata
'''