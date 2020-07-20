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


if __name__ == '__main__':
    test_copy()
