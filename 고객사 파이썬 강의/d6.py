

class A:
    def __setattr__(self, name, value):
        # return 필요 없음
        print("setattr!!")
        self.__dict__[name] = value

a = A()
a.var = 3
print(a.var)
