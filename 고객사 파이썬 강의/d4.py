

class A:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print("getattr")
        return '없습니다.'
    

a = A()

print(a.no)

a.var = 1

print(a.var)
