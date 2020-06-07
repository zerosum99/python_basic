# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 14:14:15 2016

@author: 06411
"""
import time
from datetime import datetime
from datetime import date
from datetime import timedelta



def date_call() :
    da_to = date.today()
    print " date min ", date.min, type(date.min)
    print " data max ", date.max
    print " date resolution ", date.resolution, type(date.resolution)
    print "today :", da_to
    print " strftime :", da_to.strftime("%y %m %d")    
    
    print " timestamp :", date.fromtimestamp(time.time())
    td = date.today() - date(1,1,1)
    print "time delta julian :", type(td), td.days
    print " ordinal : ", date.fromordinal(td.days+1)
    print type(timedelta.max), timedelta.min
    print " min ordinal : ", timedelta.min.days
    print " max ordinal : ", timedelta.max.days
    print " datetiem max : ", datetime.max.date()
    td_max = datetime.max.date() - date(1,1,1)
    print " max julian  : ", td_max.days
    print " max ordinal : ", date.fromordinal(td_max.days+1)
    
    
    
if __name__ == "__main__" :
    date_call()