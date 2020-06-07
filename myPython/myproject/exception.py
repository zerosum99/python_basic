# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:54:31 2016

@author: 06411
"""

class Uexcept(Exception) :
    
    def __init__(self,ex_code,ex_err) :
        self.ex_code = ex_code
        self.ex_err  = ex_err
 

def R_call() :       

    try:
        i = i + 1
    except Exception as err :
        x = Uexcept("1111",err)
        print "ex coed ",x.ex_code
        print "ex_err ", x.ex_err.message
        
        raise x
    
    
'''
try :
    R_call()
except Uexcept as err :
    print err.ex_code
    print err.ex_err
    
'''

try :
    R_call()
except Uexcept as err :
    print err.ex_code
    print err.ex_err
finally :
    print "pass"
    
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print  Argument.message
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz")

import traceback
import sys

try :
    Argument = "xxxx"
    raise Exception, Argument
except Exception, Argument :
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print " try catch ", Argument
    '''    
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=3, file=sys.stdout)
    '''
    
    s = traceback.extract_stack()
    print s
    
    

    
    