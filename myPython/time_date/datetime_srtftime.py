# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:59:38 2016

@author: 06411
"""

import datetime
 
now = datetime.datetime.now()
print(now)          # 2015-04-19 12:11:32.669083
 
nowDate = now.strftime('%Y-%m-%d')
print(nowDate)      # 2015-04-19
 
nowTime = now.strftime('%H:%M:%S')
print(nowTime)      # 12:11:32
 
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2015-04-19 12:11:32

print " strptime "
myDatetimeStr = '2015-04-15 12:23:38'
myDatetime = datetime.datetime.strptime(myDatetimeStr, '%Y-%m-%d %H:%M:%S')
print(type(myDatetime)) # [class 'datetime.datetime']
print(myDatetime)       # 2015-04-15 12:23:38

print " strptime  & replace "
yourDatetime = myDatetime.replace(day=16)
print(myDatetime)   # 2015-04-15 12:23:38
print(yourDatetime) # 2015-04-16 12:23:38

print " combine "
d = datetime.date(2015, 4, 15)
t = datetime.time(12, 23, 38)
 
dt = datetime.datetime.combine(d, t)
print(dt) # 2015-04-15 12:23:38

print " timetuple "
now2 = datetime.datetime.now()
nowTuple = now2.timetuple()
print(nowTuple)         # time.struct_time(tm_year=2015, tm_mon=4, tm_mday=19, tm_hour=13, tm_min=21, tm_sec=40, tm_wday=6, tm_yday=109, tm_isdst=-1)
print(nowTuple.tm_year) # 2016


tomorrow = now2 + datetime.timedelta(days=1)
print(tomorrow) # 2015-04-20 12:40:00.320686


oneDatetime = datetime.datetime.strptime('2015-04-15 00:00:00', '%Y-%m-%d %H:%M:%S')
twoDatetime = datetime.datetime.strptime('2015-04-16 00:00:10', '%Y-%m-%d %H:%M:%S')
result = twoDatetime - oneDatetime
print(result)         # 1 day, 0:00:10
print(result.days)    # 1
print(result.seconds) # 10