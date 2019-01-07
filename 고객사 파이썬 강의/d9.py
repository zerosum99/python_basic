

class A:
    def __delattr__(self, name):
        print("지울 수 없습니다.")
        
a = A()
a.var = 3

print(a.var)

del a.var # 여기서 __delattr__가 작동

print(a.var)
