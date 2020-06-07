# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 12:37:44 2016

@author: 06411
"""

import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Should never see this'
    
    @value.setter
    def value(self, newvalue):
        return


class Implementation(Base):
    
    # privat 처리
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue

class Implementation1(Base):
    
    # privat 처리
    _value = 'Default value1111'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue

print " 클래스 관리 영역 ", Implementation.__dict__
i = Implementation()
print 'Implementation.value:', i.value
i1 = Implementation1()
print 'Implementation.value:', i1.value

i.value = 'New value'
print 'Changed value:', i.value

i1.value = 'New value111'
print 'Changed value:', i1.value
