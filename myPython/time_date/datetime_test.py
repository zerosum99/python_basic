# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 13:29:20 2016

@author: 06411
"""

import datetime

def cal_ilsu(year,month,day) :
    start = datetime.date(year,month,day)
    end   = datetime.datetime.now()
    
    print type(start), start
    print type(end), end
    end_1 = datetime.date(end.year,end.month, end.day)
    print type(end_1), end_1
    ilsu  = end_1 - start
    print type(ilsu), ilsu.days, ilsu.seconds




if __name__ == "__main__" :
    cal_ilsu(2015,2,3)