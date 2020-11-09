import weakref


class NotInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('can not instantiate directly')


class Spam(metaclass=NotInstance):
    @staticmethod
    def spam(x):
        print('Spam.spam')
# ****************************************************************************

# 单例模式


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class OnePerson(metaclass=Singleton):
    def __init__(self):
        print('create OnePerson instance')

# ****************************************************************************


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cached = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cached:
            return self.__cached[args]
        else:
            obj = super().__call__(*args)
            self.__cached[args] = obj
            return obj


class CachedInstance(metaclass=Cached):
    def __init__(self, name):
        print('create cached instance({!r})'.format(name))
        self.name = name


if __name__ == '__main__':
    # s = Spam()

    # a = OnePerson()
    # b = OnePerson()
    # print(a, b)
    # print(a is b)

    instance1 = CachedInstance('dong')
    instance2 = CachedInstance('xiang')
    instance3 = CachedInstance('xiang')
    print(instance1 is instance2)
    print(instance2 is instance3)
