

class Person(object):
    def __init__(self, name):
        self.name = name


# p = Person('dong')
# print(p)    # <__main__.Person object at 0x000001A7B682CEE0>


class Person1(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'str person name==%s' % self.name


# p1 = Person1('dong')
# print(p1)  # str person name==dong


class Person2(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'repr person name==%s' % self.name


# p2 = Person2('dong')
# print(p2) # repr Person name==dong


class Person3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'str person name=%s' % self.name

    def __repr__(self):
        return 'repr person name==%s' % self.name


# p3 = Person3('dong')
# print(p3)
# repr Person name==dong
# str Person name=dong
