
import warnings


class Private:
    def __getattribute__(self, name, perm=False):
        if not perm:
            warnings.warn("속성에 접근할 수 없습니다.")
            return None
        return super().__getattribute__(name)

    
class ScretBox(Private):
    pass


a = ScretBox()
a.x = 3

print(a.x)
print(a.__dict__)
print(type(a).__dict__)


### 숨겨진 값을 찾기 위해서..
### 허가를 거치는 단계

print(type(a).__getattribute__(a, '__dict__', True))


from functools import partial

perm_a = partial(type(a).__getattribute__, perm=True)
print('partial 이용 : ',perm_a(a, 'x'))
