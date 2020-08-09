import random
import time


def index():
    time.sleep(random.randrange(1, 5))
    print('enter the index function...')


def calculate_times_used_in_index(index):
    def calculate():
        start_time = time.time()
        index()
        end_time = time.time()
        print('times used %s' % (end_time - start_time))
    return calculate


# 执行代码
# index = calculate_times_used_in_index(index)
# index()

# output
# enter the index function...
# times used 2.000239849090576


def calculate_times_used_in_index1(func):
    def calculate(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('times used in index==%s' % (end_time - start_time))
        return res
    return calculate


@calculate_times_used_in_index1
def index1(args):
    time.sleep(random.randrange(1, 5))
    print('parameter is %s' % args)
    return 'xiang is a genius!!!'


# 执行代码
# index1('xiang')

# output
# parameter is xiang
# times used in index==1.0004057884216309


def decorator(aClass):
    class NewClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapper = aClass(age)

        def display(self):
            self.total_display += 1
            print('total_display==', self.total_display)
            self.wrapper.display()
    return NewClass


@decorator
class Bird(object):
    def __init__(self, age):
        self.age = age

    def display(self):
        print('age==%s' % self.age)

# 执行代码
# bird = Bird(4)
# for i in range(3):
#     bird.display()

# output:
# total_display== 1
# age==4
# total_display== 2
# age==4
# total_display== 3
# age==4

##############################################################################


class MyException():
    def __init__(self):
        pass

    def receive(self):
        print('receive the message..')

    def read_value(self):
        print('read some value..')
        'a' + 1  # 这里会报异常


# ex = MyException()
# ex.read_value()  # 抛出异常


class MyException1(object):
    def __init__(self):
        pass

    def receive(self):
        print('receive the message..')

    def read_value(self):
        print('read some value..')
        try:
            'a' + 1  # 这里会报异常
        except Exception as e:
            print(e)


# ex1 = MyException1()
# ex1.read_value()

# output:
# read some value..
# can only concatenate str (not "int") to str


def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            return 'raise a exception e'
    return wrapper



class MyException2(object):
    def __init__(self):
        pass

    def receive(self):
        print('receive the message..')

    @catch_exception
    def read_value(self):
        print('read some value..')
        'a' + 1  # 这里会报异常


# ex2 = MyException2()
# print(ex2.read_value())

# output:
# read some value..
# raise a exception e


def catch_exception1(func):
    def wrapper(self, *args, **kwargs):
        try:
            res = func(self, *args, **kwargs)
            return res
        except Exception as e:
            self.receive()
            return 'raise a exception e'
    return wrapper


class MyException3(object):
    def __init__(self):
        pass

    def receive(self):
        print('receive the message..')

    @catch_exception1
    def read_value(self):
        print('read some value..')
        'a' + 1  # 这里会报异常


# ex2 = MyException2()
# print(ex2.read_value())

# output:
# read some value..
# raise a exception e


# ex3 = MyException3()
# print(ex3.read_value())

# output:
# read some value..
# receive the message..
# raise a exception e
