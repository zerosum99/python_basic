# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 16:33:47 2015

@author: 06411
"""

import sys
args = sys.argv[1:]
for i in args:
    print i



class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def sum(self):
        result = self.first + self.second
        return result
        
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

        
        
if __name__ == 'main' :
    a = FourCal()
    a.setdata(1,3)
    print " sum %d " % a.sum()
else :
    print("import call")
