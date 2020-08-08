

class Person():
    def __init__(self, name):
        self.name = name  # 会调用__setattr__

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print('enter __setattr__...')

    def __getattr__(self, item):
        print('没有要获得元素！！！')
        return self.__dict__[item]

    def __delattr__(self, item):
        print('enter delattr...')
        del self.__dict__[item]


# 执行代码
# p = Person('dong')
# print(p.name)
# p.name = 'xiang'
# print(p.name)
# print(p.age)  # 获得不存在元素时，才会进入__getattr__
# del p.name

# output
# enter __setattr__...
# dong
# enter __setattr__...
# xiang
# 没有要获得元素！！！
# enter __delattr__...


class Person1():
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        print('enter getitem...')

    def __setitem__(self, key, value):
        print('enter seitem...')


# p1 = Person1('dong')
# print(p1['name'])  # None  由于重写的__setitem__没有做事
# print(p1.__dict__) # {'name': 'dong'}
# p1['name'] = 'xiang'
# print(p1['name']) # None 由于重写的__setitem__没有做事
# print(p1.__dict__)

# output
# enter getitem...
# None
# {'name': 'dong'}
# enter seitem...
# enter getitem...
# None
# {'name': 'dong'}


class Person2():
    def __init__(self, name):
         self.name = name

    def __setitem__(self, key, value):
        print('enter setitem...')
        self.__dict__[key] = value

    def __getitem__(self, item):
        print('enter getitem...')
        return self.__dict__[item]


# 执行代码
# p2 = Person2('dong')
# print(p2['name'])
# print(p2.__dict__)
# p2['name'] = 'xiang'
# print(p2['name'])
# print(p2.__dict__)

# output
# enter getitem...
# dong
# {'name': 'dong'}
# enter setitem...
# enter getitem...
# xiang
# {'name': 'xiang'}



