# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:58:53 2016

@author: 06411
"""


class Account_Nubmer(object) :
    __Account_No = 0
    @classmethod
    def set_AN(cls) :
        cls.__Account_No +=1
        
    @classmethod
    def get_AN(cls) :
        cls.set_AN()
        return cls.__Account_No