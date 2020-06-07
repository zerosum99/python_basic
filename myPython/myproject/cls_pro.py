# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:44:13 2016

@author: 06411
"""

class P:

    def __init__(self,x):
        self.x = x
        
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    @x.deleter
    def x(self):
         del self.x         


'''     
    def getx(self) :
        return self.x
        
    def setx(self, x) :
        self.x = x
        
    def delx(self) :
        del self.x
        
    x = property(getx,setx,delx," property test ")
    print 'property',id(x)
'''


    


p1 = P(1001)
print id(p1.x)
print P.__dict__['x']
print id(p1.__dict__['x'])
print p1.x
p1.x = -12
print p1.x
print p1.__dict__