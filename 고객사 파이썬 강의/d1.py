

class A:
    x = 3
    def __getattribute__(self, name):
        print("getattribute!!!")
        return super().__getattribute__(name)
    
a = A()
a.y = 123

print(a.__dict__)
print(type(a).__dict__)
print(A.__dict__)


print(a.x)
print(a.y)
