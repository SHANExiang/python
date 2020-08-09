

class ObjectCreator(object):
    def __init__(self):
        pass


# print(ObjectCreator) # <class '__main__.ObjectCreator'>  # 类其实也是一个对象
# print(hasattr(ObjectCreator, 'attribute'))  # False
# ObjectCreator.new_attr = 'dong'
# print(hasattr(ObjectCreator, 'new_attr'))  # True
# print(ObjectCreator.new_attr)  # dong
# obj = ObjectCreator  # 可以将类赋给一个变量
# print(obj()) # <__main__.ObjectCreator object at 0x00000294C519DEE0>


#############################################################################

# 动态创建类

def create_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo  # 返回的是类
    else:
        class Bar(object):
            pass
        return Bar


Class = create_class('foo')
print(Class) # <class '__main__.create_class.<locals>.Foo'>  函数返回的是类
# <__main__.create_class.<locals>.Foo object at 0x000001BFEB9CDEE0>
print(Class()) # 通过这个类创建实例
