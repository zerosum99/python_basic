# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:02:18 2016

@author: 06411
"""

class Sandbox(object):
   def execute(self, code_string):
      
      keyword_blacklist = ["file", "open", "eval", "exec"]
      for keyword in keyword_blacklist:
          if keyword in code_string:
             raise ValueError("Blacklisted")
      
      exec code_string
      
s = Sandbox()
code = """
print "Hello world"
"""
s.execute(code)

"""
code1 = """
file("test.txt", "w").write("Kaboom!\\n")
"""

s.execute(code1)
"""

'''func = __builtins__["file"] 
#암호화해제
func = __builtins__["svyr".decode("rot13")]
func("test1.txt", "w").write("Dahl Moon!\n")
'''

code2 = """
func = __builtins__["svyr".decode("rot13")]
func("test.txt", "w").write("Dahl Moon!\\n")
"""
s.execute(code2)