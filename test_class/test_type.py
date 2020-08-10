

class GrandFather(object):pass


class Father(GrandFather):pass


class Son(Father):pass


# isinstance不止可以判断对象与实例化这个对象类的关系，还能接受“继承关系”
def test_isinstance_with_inherit():
    son = Son()
    print(isinstance(son,Son))
    print(isinstance(son,Father))
    print(isinstance(son,GrandFather))


# 只有直接实例化这个对象的类才是type(对象)的类，即使有继承关系，type也不会“承认”这个类的父类的
def test_type_with_inherit():
    son = Son()
    print(type(son))
    print(type(son) is Son)
    print(type(son) is Father)
    print(type(son) is GrandFather)

# 执行代码
    # test_isinstance_with_inherit()
    # test_type_with_inherit()


# type()方法创建类
Person = type(
    'Person',
    (object,),
    {
        'country': 'China',
        'add': lambda self, x, y: x+y
    }
)


class People1(object):
    def __init__(self, name):
        self.name = name
        # type(self)，在对象方法中使用类的方法
        self.age = type(self).get_default_age()

    @classmethod
    def get_default_age(cls):
        return 18

    def get_age(self):
        # type(self)，在对象方法中使用类的方法
        return type(self).get_default_age()


class People2(object):
    def __init__(self, name):
        self.name = name
        # type(self)，在对象方法中使用类的方法
        self.age = type(self).get_default_age(self)

    @classmethod
    def get_default_age(cls):
        return 18

    def get_age(self):
        # type(self)，在对象方法中使用类的方法
        return type(self).get_default_age(self)

    # 起一个与类方法同名的对象方法
    def get_default_age(self):
        return 20


if __name__ == '__main__':
    p1 = People1('shane')
    print(p1.get_age())  # 18
    # 对象也可以直接调用“类方法”，但是为了“规范”，我们不这么直接让对象直接调用“类方法”
    print(p1.get_default_age())  # 18

    # 如果对象方法与类方法同名的话，对象会优先调用自己的方法
    p2 = People2('shane')
    print(p2.get_age())  # 20
    print(p2.get_default_age()) # 20