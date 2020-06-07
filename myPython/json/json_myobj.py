# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:24:57 2016

@author: 06411
"""
#json_myobj.py

class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s