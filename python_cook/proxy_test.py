

class A(object):
    def spam(self, num):
        print('do something...', num)


class B(object):
    def __init__(self):
        self._a = A()

    def spam(self, num):
        self._a.spam(num)

# ****************************************************************************


class B2(object):
    def __init__(self):
        self._a = A()

    # def spam(self, num):
    #     pass

    def __getattr__(self, item):
        return getattr(self._a, item)

# ****************************************************************************


class Proxy(object):
    def __init__(self, obj):
        self._obj = obj

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setattr:', key, value)
            setattr(self._obj, key, value)

    def __getattr__(self, item):
        print('getattr:', item)
        return getattr(self._obj, item)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


class Spam(object):
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print("Spam.bar:", self.x, y)


if __name__ =='__main__':
    # b = B()
    # b.spam(3)

    # b2 = B2()
    # b2.spam(3)

    spam = Spam(2)
    proxy = Proxy(spam)
    print(proxy.bar)
    proxy.bar(4)
