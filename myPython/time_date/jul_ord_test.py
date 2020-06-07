# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 16:59:06 2016

@author: 06411
"""

import datetime

def cal_julian(year,month,day) :
    start = datetime.date(year,month,day)
    print ' start day : ', start
    end   = datetime.date.today()
    print ' end   day : ', end
    
    
    time_delta  = end - start
    print ' julian day : ', time_delta.days
    
    return (start,time_delta.days)
   
    
def cal_ordinal(start) :
    x, y = cal_julian(1,1,1)
    ordinal = y  +1
    print " today  :", datetime.date.fromordinal(ordinal)
    

if __name__ == "__main__" :
    start,julian_day = cal_julian(2015,2,3)
    cal_ordinal(start)