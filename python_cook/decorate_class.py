from functools import wraps
import types


class Profiled(object):
    def __init__(self, func):
        wraps(func)(self)
        self.ncall = 0

    def __call__(self, *args, **kwargs):
        self.ncall += 1
        self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Test(object):
    @Profiled
    def spam(self):
        print('spam')


if __name__ == '__main__':
    add(1, 2)
    test = Test()
    test.spam()
