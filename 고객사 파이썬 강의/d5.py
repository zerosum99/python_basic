

class Meta(type):
    def __getattribute__(self, name):
        return "classattribute"
    
    def __getattr__(self, name):
        return "classattr"
    

class A(metaclass=Meta):
    pass


#print(A.b)
a = A()
print(a.b)
