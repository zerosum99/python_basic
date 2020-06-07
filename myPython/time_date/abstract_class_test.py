# -*- coding: utf-8 -*-
"""
Created on Fri Feb 05 09:08:58 2016

@author: 06411
"""
from abc import ABCMeta, abstractmethod

#3.x버전 class BaseABC(metaclass=ABCMeta):
class BaseABC():
    __metaclass__= ABCMeta
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class ConcreteABC(BaseABC):
    def foo(self):
        print " foo pass"
    def bar(self):
        print " bar pass"

#excetion 기준의 추상클래스 처리하기
class Base:
    def foo(self):
        raise NotImplementedError("foo")

    def bar(self):
        raise NotImplementedError("bar")
        
class Concrete(Base):
    def foo(self):
        return "foo() called"       
    
def abc_abs() :
   
    try :
       # 인스턴스 생성부터 에러처리 필요
       b = BaseABC()
       b.bar()
    except Exception, e :
        print 'exception ',e.message
    except TypeError, e :
        print 'NotImplementedError ', e.message
    finally :
        print " abc "
            
    c = ConcreteABC()
    print c.foo()  
    print c.bar()
    
def except_abs() :
    b = Base()
    try :
       b.bar()
    except Exception, e :
        print 'exception ',e.message
    except NotImplementedError, e :
        print 'NotImplementedError ', e.message
    finally :
        print " abc "
        
    c = Concrete()
    print c.foo()  
    print c.bar()
    
if __name__ == "__main__" : 
   # except 처리  
   try :  
       except_abs()
   except Exception, e :
        print 'exception ',e.message
   # abc 모듈 처리 
   try :
      abc_abs()
   except Exception, e :
        print 'exception ',e.message
        
   print issubclass(Concrete, Base)


    