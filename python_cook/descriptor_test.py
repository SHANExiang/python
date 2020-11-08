

class Integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('not int type')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Description(object):
    def __init__(self, name=None, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Description):
    expect_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError('Excepted type %s' % self.expect_type)
        super().__set__(instance, value)


class Unsigned(Description):
    def __set__(self, instance, value):
        if value < 0:
            raise TypeError('Excepted >= 0')
        super().__set__(instance, value)


class MaxSized(Description):
    def __init__(self, name=None, **kwargs):
        if 'size' not in kwargs:
            raise TypeError("missing size option")
        super().__init__(name, **kwargs)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size mush be < ' + str(self.size))
        super().__set__(instance, value)


class MyInteger(Typed):
    expect_type = int


class MyFloat(Typed):
    expect_type = float


class IntegerUnsigned(MyInteger, Unsigned):
    pass


class FloatUnsigned(MyFloat, Unsigned):
    pass


class MyString(Typed):
    expect_type = str


class SizedString(MaxSized, MyString):
    pass


class Stock(object):
    name = SizedString('name', size=8)
    shares = IntegerUnsigned('shares')
    price = FloatUnsigned('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
# ***********************************************************************


if __name__ == '__main__':
    # point = Point(2, 3)
    # print(point.x)
    # print(point.y)
    # point.y = 6
    # print(point.y)
    # point.x = 3.6

    stock = Stock('dong', 20, 1.2)
    print(stock.__dict__)
    # stock.name = 'xiangsfggdgd '   # 报错 size mysh be <8
    # stock.price = -2   # 报错 Excepted type <class 'float'>

