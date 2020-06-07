# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:29:06 2016

@author: 06411
"""

from datetime import time, tzinfo,timedelta

#tzinfo 추상클래스를 현행화
class GMT1(tzinfo):
   def utcoffset(self, dt):
      return timedelta(hours=1)
   def dst(self, dt):
      return timedelta(0)
   def tzname(self,dt):
      return "Europe/Prague"
 
#시간생성  tzinfo에 객체 생성    
t = time(12, 10, 30, tzinfo=GMT1())
print "time instance   : ",t
print "time iso format : ",t.isoformat()
print "time dst        : ", t.dst()
print 'time zone       : ',t.tzname()
print "time strftime   : ",t.strftime("%H:%M:%S %Z")
print 'The {} is {:%H:%M}.'.format("time", t)
