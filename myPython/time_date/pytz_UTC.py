# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:13:50 2016

@author: 06411
"""

"""
@instancemethod
dst(self, dt): int
fromutc() : int
localize(self,dt) : str
normalize() : str
utcoffset() :
tzname() :

"""

import pytz
import datetime


print "pytz.UTC ", type(pytz.UTC), pytz.UTC, issubclass(type(pytz.UTC), datetime.tzinfo)
print "pytz.UTC.zone ", type(pytz.UTC.zone), pytz.UTC.zone
print "pytz.UTC.tzname ", pytz.UTC.tzname
print "pytz.UTC formutc method ", pytz.UTC.fromutc(datetime.datetime.utcnow())

utc = pytz.utc
print "pytz.utc dst method ", utc.dst(datetime.datetime.utcnow())
print "pytz.utc utcoffset method ", utc.utcoffset(datetime.datetime.utcnow())
print "pytz.utc localize method ", utc.localize(datetime.datetime.utcnow())
print "pytz.utc normalize method ", utc.normalize(datetime.datetime.now(tz=pytz.timezone("Asia/Seoul")))


korean = pytz.timezone('Asia/Seoul')

print type(korean)
print "datatime.tzinfo subclass ",issubclass(type(korean), datetime.tzinfo)
print " Asia/Seoul time zone ", korean.localize(datetime.datetime.now())
korean_dt = korean.localize(datetime.datetime.now())
print " korean_dt type ", type(korean_dt)
print "datatime.datetime.astimezone normalize "
print "type ", korean_dt.astimezone(pytz.timezone('US/Eastern'))
eastern = korean_dt.astimezone(pytz.timezone('US/Eastern'))
print " time zone change ", eastern

amsterdam = pytz.timezone('Europe/Amsterdam')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
print datetime.datetime(2002, 10, 27, 12, 0, 0, tzinfo=amsterdam)
print datetime.datetime(2002, 10, 27, 12, 0, 0, tzinfo=amsterdam).strftime(fmt)

print(pytz.country_names['nz'])
for zzz in pytz.country_names :
    print zzz
print(' '.join(pytz.country_timezones['nz']))

print type(pytz.utc)
print type(pytz.country_names)