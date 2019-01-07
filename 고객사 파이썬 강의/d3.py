

import warnings


class A:
    def __getattr__(self, name):
        warnings.warn("값이 없습니다. 디폴트값을 넘깁니다.")
        return 3

a = A()
a.var = 123
print('a.var', a.var)
print('a.xxx', a.xxx)
