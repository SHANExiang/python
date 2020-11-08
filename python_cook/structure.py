

class Structure(object):
    _fields = []

    # 只有可变参数args
    # def __init__(self, *args):
    #     if len(self._fields) != len(args):
    #         raise TypeError("Excepted {} arguments".format(len(self._fields)))
    #     for key, value in zip(self._fields, args):
    #         setattr(self, key, value)

    # 增加判断关键字参数
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Excepted {} arguments'.format(len(self._fields)))
        for key, value in zip(self._fields, args):
            setattr(self, key, value)

        for key in self._fields[len(args):]:
            setattr(self, key, kwargs.pop(key))

        if kwargs:
            raise TypeError('Invalid arguments {}'.format(','.join(kwargs)))


class Point(Structure):
    _fields = ['x', 'y', 'z']


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


if __name__ == '__main__':
    # point = Point(1, 2, 3) # 实例化时必须传3给参数
    # print(point)
    stock1 = Stock('dong', 50, 23.1)
    stock2 = Stock('dong', shares=50, price=23.1)
    stock3 = Stock('dong', 50, price=23.1)
    print(vars())
