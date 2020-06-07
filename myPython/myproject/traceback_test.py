# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:02:54 2016

@author: 06411
"""

import sys
import traceback

def func1():
    func2()

def func2():
    raise Exception('test error')

def main():

    try:
        func1()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # Do your verification using exc_value and exc_traceback

        print "*** print_exception:"
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=3, file=sys.stdout)
    
main()




try:
    1/0
except Exception as e:
    print 'the relevant part is: '+ traceback.format_exc() #.split('\n')[-2]
    print "exception print : " + e.message