import math


class Lazyproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('compute circle area')
        return math.pi * self.radius ** 2

    @Lazyproperty
    def perimeter(self):
        print('compute perimeter')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    circle = Circle(3)
    print(circle.area)
    print(circle.area)
    print(circle.perimeter)
    print(circle.perimeter)
    circle.radius = 4
    print(circle.area)
    print(circle.area)
    print(circle.perimeter)
    print(circle.perimeter)
