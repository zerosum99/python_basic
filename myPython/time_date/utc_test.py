# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:22:05 2016

@author: 06411
"""

from datetime import datetime
from pytz import timezone
import pytz
utc = pytz.utc
print ' utc ', utc
print utc.zone  #'UTC'
eastern = timezone('US/Eastern')
print ' eastern type ', eastern
print eastern.zone #'US/Eastern'
amsterdam = timezone('Europe/Amsterdam')

fmt = '%Y-%m-%d %H:%M:%S %Z%z' 

loc_dt = eastern.localize(datetime(2002, 10, 27, 6, 0, 0))
print(loc_dt.strftime(fmt)) #2002-10-27 06:00:00 EST-0500

ams_dt = loc_dt.astimezone(amsterdam)
print(ams_dt.strftime(fmt))

print datetime(2002, 10, 27, 12, 0, 0, tzinfo=amsterdam).strftime(fmt)

from pytz import all_timezones

print len(all_timezones)
for zone in all_timezones:
    #if 'US' in zone:
    print zone