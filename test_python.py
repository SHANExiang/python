import copy
import sys


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


# 闭包                       **************************------------------------
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


# 装饰器                      **************************------------------------
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


# random模块使用              **************************------------------------
import random
# 生成一个范围内的随机数
# print(random.randrange(1, 10))   # 左开右闭,不包括10
# print(random.randrange(1, 20, 3))   # 1-20之间，步长为3的数字
# print(random.randint(1, 10))   # 1-10之间的整数，包括10
# print(random.choice('dongxiang1243'))   # 在一个字符串中间选择一个
# print(random.choice((1, 2, 34, '34')))   # 返回一个给定数据集合的随意数据
# print(random.sample('shanedfgv2335', 4))   # 返回给定数量的数据集合的列表
# print(random.sample([2, 34, '34', 3], 4))   # 返回给定数量的数据集合的列表
# l = [3, 4, 5, 6, 7]
# random.shuffle(l)
# print(l)     # 打乱数据集合


# 函数中修改列表以及列表中的元素 **************************------------------------
lis = [1, 2, 3, 4, 5]
# print(id(lis))


def change_list1():
    # 此lis与外边的lis作用域不一样，这是局部变量, 这个意思是将存放[1, 2, 3]这个列表的内存
    # 地址赋给了lis，而lis这个变量已经指向了[1, 2, 3, 4, 5]这个内存地址，
    # print(id(lis))   # 要是局部变量与全局变量名称一致时，函数中只认此局部变量
    lis = [1, 2, 3]
    print(id(lis))


# change_list1()
# print(lis)


def change_list2():
    global lis   # 只有在函数中利用global关键字声明后才能修改全局变量
    print(id(lis))
    lis = [1, 2, 3]  # 相当于此lis变量就是全局变量lis
    print(id(lis))


# change_list2()
# print(lis)


def change_list3():
    print(id(lis))
    lis.append(6)
    del lis[0]
    l = lis
    print(l)

# 函数中可以改变全局列表变量中的值，但不能修改其引用，除非加上global
# 对于列表、字典、集合这样的数据结构以及类、对象中的元素我们都可以在函数中修改；
# 而对于数字、字符串这样的数据类型只有在函数中利用global关键字声明后才能对全局变量进行修改！
# change_list3()
# print(lis)    # [2, 3, 4, 5, 6]


# sys.modules[__name__]      **************************------------------------


def function():
    print('test sys.modules')


# print(sys.modules[__name__])   # 此python文件中的module 'main'
# print(function.__name__)    # 函数名
# function_obj = getattr(sys.modules[__name__], function.__name__)# 获得此函数名对象
# function_obj()


# 互斥锁                      **************************------------------------
import json
import os
import time
from multiprocessing import Process, Lock, Queue


def remain(ticket_name, ticket_buyer):
    time.sleep(1)
    with open('tickets.json', 'r', encoding='utf-8') as f:
        tickets_dict = json.load(f)
        tickets_remain = tickets_dict.get(ticket_name)
        if tickets_remain <= 0:
            print('<%s>查看%s 余票不足...' % (ticket_buyer, ticket_name))
        else:
            print('<%s>查看remain tickets numbers==%s' % (ticket_buyer,
                                                        tickets_remain))


def buy_tickets(ticket_name, ticket_buyer):
    time.sleep(1)
    with open('tickets.json', 'r', encoding='utf-8') as f:
        tickets_dict = json.load(f)
        tickets_remain = tickets_dict.get(ticket_name)
    tickets_remain -= 1
    with open('tickets.json', 'w', encoding='utf-8') as f:
        if tickets_remain >= 0:
            tickets_dict = {'%s' % ticket_name : tickets_remain}
            json.dump(tickets_dict, f, ensure_ascii=False)
            print('<%s>购买到票' % ticket_buyer)
        else:
            tickets_dict = {'%s' % ticket_name: 0}
            json.dump(tickets_dict, f, ensure_ascii=False)
            print('<%s>未购买到票' % ticket_buyer)


def task(ticket_name, ticket_buyer, mutex):
    remain(ticket_name, ticket_buyer)
    mutex.acquire()
    buy_tickets(ticket_name, ticket_buyer)
    mutex.release()


# with open('tickets.json', 'w', encoding='utf-8') as f:
#     json.dump({'速度与激情7': 4}, f, ensure_ascii=False)
# file_new = open('tickets.json', 'r', encoding='utf-8')
# print(file_new.read())
# file_new.close()

# 执行代码  只能在__name__=='__main__'中执行
#     mutex = Lock()
#     for i in range(4):
#         p = Process(target=task, args=('速度与激情7', '学生%s' % (i + 1), mutex))
#         p.start()


def producer(queue):
    for i in range(4):
        res = '商品%s' % (i + 1)
        time.sleep(0.5)
        print('生产者%s生产%s' % (os.getpid(), res))
        queue.put(res)


def consumer(queue):
    while True:
        res = queue.get()
        if not res:
            break
        time.sleep(1)
        print('消费者%s消费了%s' % (os.getpid(), res))

# 执行代码
#     q = Queue()
#     p1 = Process(target=producer, args=(q, ), name='p1')
#     p2 = Process(target=producer, args=(q, ), name='p2')
#     c1 = Process(target=consumer, args=(q, ), name='c1')
#     c2 = Process(target=consumer, args=(q, ), name='c2')
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     p1.join()
#     p2.join()
    # 以下put两个None是为了让两个消费者停止消费，跳出循环
    # q.put(None)
    # q.put(None)


# 线程属性和方法               **************************------------------------
import threading
from threading import current_thread, enumerate, active_count
# print(current_thread().getName())
# print(active_count())
# print(enumerate())


def worker():
    print('os.get_pid==%s' % os.getpid())
    print('the thread is working...')
    print(current_thread().getName(), 'is in worker')
    print(current_thread().is_alive())

# 执行过程
    # thread1 = threading.Thread(target=worker, name='thread1')
    # thread1.start()
    # thread1.join()
    # print(thread1.getName())
    # print(thread1.is_alive())
    # thread1.setName('thread1_to_update')
    # print(thread1.getName())

# python几种加密方式           **************************------------------------


# base64
import base64


def test_base64():
    encode_str = base64.b64encode(b'dongxiang is a genius!!!')
    print('encode_str==%s' % encode_str)
    decode_str = base64.b64decode(encode_str)
    print('decode_str==%s' % decode_str)

# 执行代码
#     test_base64()

# md5
import hashlib


def test_md5(string):
    h1 = hashlib.md5()
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 此处必须声明encode
    h1.update(string.encode('utf-8'))
    print('string 加密前==%s' % string)
    print('string 加密后==%s' % h1.hexdigest())

# 执行代码
#     test_md5('dong xiang is a genius!!!')

# AES
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex


def test_AES(string):
    key = b'xiangdong1234567'
    iv = Random.new().read(AES.block_size)
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    encrypt = mycipher.encrypt(string.encode())
    cipher_text = iv + encrypt
    mydecrypt = AES.new(key, AES.MODE_CFB, cipher_text[:16])
    decrypt_text = mydecrypt.decrypt(cipher_text[16:])
    print('密匙是==%s' % key)
    print('iv==%s, len(iv)==%s' % (iv, len(iv)))
    print('encrypt==%s' % b2a_hex(encrypt).decode())
    print('加密后数据为==%s' % b2a_hex(cipher_text[16:]).decode())
    print('解密后数据为==%s' % decrypt_text.decode())

# 执行代码
#     test_AES('dong xiang 0816')


if __name__ == '__main__':
    pass




