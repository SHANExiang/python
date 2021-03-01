import gevent
from gevent import monkey
import time


def func1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


# g1 = gevent.spawn(func1, 5)
# g1.join()
# <Greenlet at 0x277bec678c0: func1(5)> 0
# <Greenlet at 0x277bec678c0: func1(5)> 1
# <Greenlet at 0x277bec678c0: func1(5)> 2
# <Greenlet at 0x277bec678c0: func1(5)> 3
# <Greenlet at 0x277bec678c0: func1(5)> 4


def func2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def func3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


# g1 = gevent.spawn(func1, 5)
# g2 = gevent.spawn(func2, 5)
# g3 = gevent.spawn(func3, 5)
#
# g1.join()
# g2.join()
# g3.join()

# <Greenlet at 0x1da0fa898c0: func1(5)> 0
# <Greenlet at 0x1da0fa89ae0: func2(5)> 0
# <Greenlet at 0x1da0fa899d0: func3(5)> 0
# <Greenlet at 0x1da0fa898c0: func1(5)> 1
# <Greenlet at 0x1da0fa89ae0: func2(5)> 1
# <Greenlet at 0x1da0fa899d0: func3(5)> 1
# <Greenlet at 0x1da0fa898c0: func1(5)> 2
# <Greenlet at 0x1da0fa89ae0: func2(5)> 2
# <Greenlet at 0x1da0fa899d0: func3(5)> 2
# <Greenlet at 0x1da0fa898c0: func1(5)> 3
# <Greenlet at 0x1da0fa89ae0: func2(5)> 3
# <Greenlet at 0x1da0fa899d0: func3(5)> 3
# <Greenlet at 0x1da0fa898c0: func1(5)> 4
# <Greenlet at 0x1da0fa89ae0: func2(5)> 4
# <Greenlet at 0x1da0fa899d0: func3(5)> 4


monkey.patch_all()


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(0.5)


gevent.joinall([
    gevent.spawn(coroutine_work, 'work1'),
    gevent.spawn(coroutine_work, 'work2'),
    gevent.spawn(coroutine_work, 'work3'),
])
