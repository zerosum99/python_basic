# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:27:34 2016

@author: 06411
"""

import sys

# it's easy to print this list of course:
print sys.argv

# or it can be iterated via a for loop:

for i in range(len(sys.argv)):
    if i == 0:
        print "Function name: %s" % sys.argv[0]
    else:
        print "%d. argument: %s" % (i,sys.argv[i])