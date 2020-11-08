

class Parent(object):
    def spam(self):
        print('parent spam...')


class Son(Parent):
    def spam(self):
        super().spam()
        print('son spam...')


class A(object):
    def __init__(self):
        self.x = 10


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


class Person():
    def __init__(self, name):
        self.name = name


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


if __name__ == '__main__':
    # son = Son()
    # son.spam()

    # b = B()
    # print(b.x)
    # print(b.y)
    # a = A()
    # print(a.x)

    person = Person('dng')
    p = Proxy(person)
    print(p.__getattr__('name'))
    p.__setattr__('name', 'dongxiang')
    print(p.__getattr__('name'))
