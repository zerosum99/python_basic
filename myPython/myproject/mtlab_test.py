# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:00:31 2016

@author: 06411
"""

from pylab import *

x = linspace(-1.6, 1.6, 10000)
f = lambda x: (sqrt(cos(x)) * cos(200 * x) + sqrt(abs(x)) - 0.7) * \
    pow((4 - x * x), 0.01)
plot(x, map(f, x))
show()