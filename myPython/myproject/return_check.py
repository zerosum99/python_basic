# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:03:04 2016

@author: 06411
"""

type_str = ['str','int','float','list','dict','function','object']

def return_type(obj) :
    
    type_check = obj.__class__.__name__
    if type_check in type_str :
        return True, type_check
    else :
        return False, type_check