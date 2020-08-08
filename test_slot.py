

class Person(object):
    __slots__ = {'name': 'dong', 'age': 20}

    def __init__(self, name):
        self.name = name


p1 = Person('p1')
print('p1.__slot__==%s, 以及p1.__slot__内存地址==%s, ' %
      (p1.__slots__, id(p1.__slots__)))
p2 = Person('p2')
print('p2.__slot__==%s, 以及p2.__slot__内存地址==%s, ' %
      (p2.__slots__, id(p2.__slots__)))

# output:
# p1.__slot__=={'name': 'dong', 'age': 20}, 以及p1.__slot__内存地址==2042154602816,
# p1.__slot__=={'name': 'dong', 'age': 20}, 以及p1.__slot__内存地址==2042154602816,


class Person1(object):
    prop = 'wuming'

    def __init__(self, name):
        self.name = name


p3 = Person1('p3')
print('p3.__dict__==%s, 以及p3.__dict__内存地址==%s, ' %
      (p3.__dict__, id(p3.__dict__)))
p4 = Person1('p4')
print('p4.__dict__==%s, 以及p4.__dict__内存地址==%s, ' %
      (p4.__dict__, id(p4.__dict__)))

# output:
# p3.__dict__=={'name': 'p3'}, 以及p3.__dict__内存地址==2042154602752,
# p4.__dict__=={'name': 'p4'}, 以及p4.__dict__内存地址==2042155447744,
