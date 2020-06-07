# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:12:44 2015

@author: 06411
"""

a = 0
while a < 10:
    a = a + 1
    print a
    
s = type(a)
print s
print type(s)
#줄리안 일수 전환
def dayconvert(month) :
    
        convertDay = 0
        
        dayDict = {'01':0, '02':31, '03':59, '04':90, '05':120,
                   '06':151, '07':181, '08':212, '09':243, '10':273,
                   '11':304, '12':334}
       
        convertDay = dayDict[month]
        return convertDay
#줄리안데이 산출
def julian(date):
    
    year = int(date[0:4])
    month = date[4:6]
    day   = int(date[6:8])
       
    yuncheck = yunyear(year) 
      
    Dday = dayconvert(month)
    Dday = Dday + day
    
    if yuncheck == 1:
             if int(month) > 2 :
                 Dday =  Dday + 1
    
    if Dday < 100 :
        Dday = '0' + str(Dday)
    else :
        pass
    
    date1 = str(year) + str(Dday)
    return date1
 #윤년 체크   
def yunyear(year) :
    intyear = int(year)
    if intyear % 4 == 0 :
        if intyear % 100 == 0 :
            if intyear % 400 == 0 :
                yuncheck = 1
            else:
                yuncheck = 2
        else:
            yuncheck = 1
    else:
        yuncheck =2
    return yuncheck
    
print julian('20120301')
print yunyear('2012')