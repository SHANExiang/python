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


