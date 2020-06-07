# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:27:02 2016

@author: 06411
"""

class rectangle() :
    def __init__(self,height, width) :
        if height == width :
           self.height = height
           self.width  = width
        else : 
            if self.__class__.__name__ == 'square' :
                print " error "
            else :
                self.height = height
                self.width  = width
        
    def area(self) :
        return self.height * self.width

class square(rectangle) :
    pass
'''    
    def __init__(self,height, width) :
       
        rectangle.__init__(self,height, width)
  
    def area(self) :
        return self.height * self.width
''' 
  

r = rectangle(5,8)
print r.__dict__
print r.area()

try :
    s = square(5,6)
    print s.__dict__
    print s.area()
except :
    pass
