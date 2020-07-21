import copy


# 深拷贝与浅拷贝
def test_copy():
    # 列表的深、浅拷贝
    list1 = [2, 3, 4, 5, 6]
    list2 = list1
    list1.append(90)
    print('list1地址==%s, list2地址==%s' % (id(list1), id(list2)))
    print('list1索引2的元素地址==%s, list2索引2的元素地址==%s' %
          (id(list1[2]), id(list2[2])))
    list2[2] = 34
    print('list1==%s, list2==%s' % (list1, list2))
    print('list1索引2的元素地址==%s, list2索引2的元素地址==%s' %
          (id(list1[2]), id(list2[2])))
    list1.append([2, 3])
    print('list1==%s, list2==%s' % (list1, list2))
    print('list1索引2的元素地址==%s, list2索引2的元素地址==%s' %
          (id(list1[2]), id(list2[2])))
    list2[6].append(3)
    print('list1==%s, list2==%s' % (list1, list2))
    print('list1索引2的元素地址==%s, list2索引2的元素地址==%s\n' %
          (id(list1[2]), id(list2[2])))

    # 浅拷贝
    list3 = [1, 2, 3, [4, 5]]
    # list4 = list3.copy()
    list4 = copy.copy(list3)
    print('list3地址==%s, lis4地址==%s' % (id(list3), id(list4)))
    print('list3索引2的元素地址==%s, list4索引2的元素地址==%s' %
          (id(list3[2]), id(list4[2])))
    list4[2] = 100
    list3[1] = 90
    print('list3==%s, list4==%s' % (list3, list4))
    list3[2] = 100
    print('list3索引2的元素地址==%s, list4索引2的元素地址==%s' %
          (id(list3[2]), id(list4[2])))
    # 浅拷贝列表中的列表的地址是一样的，如果改动就影响整个
    list3[3].append(6)
    list4[3].append(7)
    list3[3][2] = 100
    print('list3==%s, list4==%s' % (list3, list4))
    print('list3索引3的元素地址==%s, list4索引3的元素地址==%s\n' %
          (id(list3[3]), id(list4[3])))

    # 深拷贝
    list5 = [1, 2, 3, [4, 5]]
    list6 = copy.deepcopy(list5)
    print('list5地址==%s, list6地址==%s' % (id(list5), id(list6)))
    print('list5索引2的元素地址==%s, list6索引2的元素地址==%s' %
          (id(list5[2]), id(list6[2])))
    list5[2] = 100
    list6[1] = 90
    print('list5==%s, list6==%s' % (list5, list6))
    list6[2] = 100
    print('list5索引2的元素地址==%s, list6索引2的元素地址==%s' %
          (id(list5[2]), id(list6[2])))
    print('list5索引3的元素地址==%s, list6索引3的元素地址==%s' %
          (id(list5[3]), id(list6[3])))
    # 深拷贝列表中的列表的地址是不一样的，如果改动对另外个不影响
    list5[3].append(6)
    list6[3].append(7)
    list5[3][2] = 100
    print('list5==%s, list6==%s' % (list5, list6))
    print('list5索引3的元素地址==%s, list6索引3的元素地址==%s\n' %
          (id(list5[3]), id(list6[3])))

    # 字典的深、浅拷贝
    dict1 = {'a': 23, 'b': 34, 'c': [1, 2, 3]}
    dict2 = copy.copy(dict1)
    print('dict1==%s, dict2==%s, dict1["c"]内存地址==%s, dict2["c"]内存地址==%s'
          % (dict1, dict2, id(dict1['c']), id(dict2['c'])))
    dict1['c'].append(4)
    dict2['c'].append(5)
    print('dict1==%s, dict2==%s, dict1["c"]内存地址==%s, dict2["c"]内存地址==%s'
          % (dict1, dict2, id(dict1['c']), id(dict2['c'])))
    dict3 = {'a': 23, 'b': 34, 'c': [1, 2, 3]}
    dict4 = copy.deepcopy(dict3)
    print('dict3==%s, dict4==%s, dict3["c"]内存地址==%s, dict4["c"]内存地址==%s'
          % (dict3, dict4, id(dict3['c']), id(dict4['c'])))
    dict3['c'].append(4)
    dict2['c'].append(5)
    print('dict3==%s, dict4==%s, dict3["c"]内存地址==%s, dict4["c"]内存地址==%s'
          '\n' % (dict3, dict4, id(dict3['c']), id(dict4['c'])))

    # 元组的深、浅拷贝
    # 注意：元组不能直接tuple2 = tuple1.copy(),因为没有这个方法
    tuple1 = (1, 2, 3, 4, [5, 6])
    tuple2 = copy.copy(tuple1)
    print('tuple1==%s, tuple2==%s' % (tuple1, tuple2))
    print('tuple1内存地址==%s, tuple2内存地址==%s, tuple1[2]内存地址==%s, '
          'tuple2[2]内存地址==%s' % (id(tuple1), id(tuple2), id(tuple1[2]),
                                                            id(tuple2[2])))
    tuple1[4].append(7)
    tuple2[4].append(8)
    print('tuple1==%s, tuple2==%s' % (tuple1, tuple2))
    print('tuple1内存地址==%s, tuple2内存地址==%s, tuple1[4]内存地址==%s, '
          'tuple2[4]内存地址==%s\n' % (id(tuple1), id(tuple2), id(tuple1[4]),
                                 id(tuple2[4])))
    # tuple1[2] = 100   元素是不可变数据类型，不能改变其值,也能增加值，也不能删除，
    # del tuple1[2] tuple[5] = 100 报错TypeError: 'tuple' object doesn't support item deletion
    tuple3 = (1, 2, 3, 4, [5, 6])
    tuple4 = copy.deepcopy(tuple3)
    print('tuple3==%s, tuple4==%s' % (tuple3, tuple4))
    print('tuple3内存地址==%s, tuple4内存地址==%s, tuple3[2]内存地址==%s, '
          'tuple4[2]内存地址==%s' % (id(tuple3), id(tuple4), id(tuple3[2]),
                                 id(tuple3[2])))
    tuple3[4].append(7)
    tuple4[4].append(8)
    print('tuple3==%s, tuple4==%s' % (tuple3, tuple4))
    print('tuple3内存地址==%s, tuple4内存地址==%s, tuple3[4]内存地址==%s, '
          'tuple4[4]内存地址==%s' % (id(tuple3), id(tuple4), id(tuple3[4]),
                                 id(tuple4[4])))

# test_copy()


# 闭包
# 调用func的时候就产生了闭包（inner_func+name），这意味着当func声明周期结束的时候，name
# 这个变量依旧存在，因为它被闭包引用了，所以不会被回收。
# 所谓闭包---在函数内部定义一个函数，并且这个函数用到了外部函数的变量，那么讲这个函数与用到
# 的一些变量称为闭包。
def func(name):
    def inner_func(age):
        print('%s的年龄为%s' % (name, age))
    return inner_func
#      f = func('shane')
#      f(20)
#      print('函数inner_func的内部地址为%s' % f)


# 装饰器
# 1. 不带参数的装饰器
def wrap1(func):
    def inner_func(*args, **kwargs):
        print('I\'m inner_func', args, kwargs)
        func()
    return inner_func


# 也就是说我们在进行不带参数的装饰器的调用时，相当于把下面的函数名当做参数传给了@后面的函数
@wrap1   # 等价于 func1 = wrap(func1),
def func1():
    print('I\'m func1...')
# func1()
# func1('dong', 'xiang', name='dongxiang')


# 2. 带参数的装饰器
def wrap2(type):
    def outer(func):
        def inner(*args, **kwargs):
            if type == 'apple':
                print('apple phone!!!')
                func(*args, **kwargs)
            else:
                print('other phone!!!')
        return inner
    return outer


# 如果要返回函数的话，带参数的装饰器就要写三层内嵌函数。
# 等价于func2 = wrap2('apple')(func)
@wrap2('apple')
def func2():
    print('func2....')
# func2()


# random模块使用
import random
# 生成一个范围内的随机数
print(random.randrange(1, 10))   # 左开右闭,不包括10
print(random.randrange(1, 20, 3))   # 1-20之间，步长为3的数字
print(random.randint(1, 10))   # 1-10之间的整数，包括10
print(random.choice('dongxiang1243'))   # 在一个字符串中间选择一个
print(random.choice((1, 2, 34, '34')))   # 返回一个给定数据集合的随意数据
print(random.sample('shanedfgv2335', 4))   # 返回给定数量的数据集合的列表
print(random.sample([2, 34, '34', 3], 4))   # 返回给定数量的数据集合的列表
l = [3, 4, 5, 6, 7]
random.shuffle(l)
print(l)     # 打乱数据集合



# if __name__ == '__main__':
#     pass
