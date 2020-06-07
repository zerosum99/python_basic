# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 13:15:41 2016

@author: 06411
"""

import time

def time_call() :
    t = time.localtime()
    print type(t)
    print "%d %d %d" % (t.tm_year,t.tm_mon, t.tm_mday)
    print " time str ", time.strftime("%Y-%m-%d")
    


if __name__ == "__main__" :
    time_call()

