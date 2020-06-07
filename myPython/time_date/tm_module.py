# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:32:57 2016

@author: 06411
"""

import time
import pytz
import datetime

tz = time.tzname
print time.timezone
print tz
print tz[0]
print tz[0].decode('euc-kr')

print pytz.all_timezones

for tzs in pytz.all_timezones :
    if 'Asia/Seoul' in tzs :
        tzs_seoul = tzs
    if 'America/New_York' in tzs :
        tzs_newyork = tzs
        
print ' tzs new york '     
EST = pytz.timezone(tzs_newyork)

print " ETS  type ", type(EST)
dt1 = datetime.datetime.now(tz=EST)
print " tzs new off ", EST.utcoffset(datetime.datetime.now())
print " tzs new loc ", EST.localize(datetime.datetime.now())
print " tzs new nor ", EST.normalize(datetime.datetime.now(tz=EST))
print ' tzs newyork', dt1

EST2 = pytz.timezone(tzs_seoul)
print " ETS 2 type ", type(EST2)
dt2 = datetime.datetime.now(tz=EST2)
print " seoul date time ", dt2

print datetime.datetime.today()
dtdt = datetime.datetime.now()
print dtdt

EST = pytz.timezone('America/New_York')
EST2 = pytz.timezone('Asia/Seoul')
ts1 = datetime.datetime.now(tz=EST)
print ' type ', type(ts1)
print ' time info ', ts1.tzinfo
print ' time zone ', ts1.timetz()
ts2 = datetime.datetime.now(tz=EST2)
print ts1
print ts2


