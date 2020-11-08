import time
from functools import wraps


def timedelta(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__, end_time - start_time)
        return result
    return wrapper


@timedelta
def countdown(n):
    print('enter countdown')
    while n > 0:
        n -= 1


def countdown2(n):
    while n > 0:
        n -= 1

# ****************************************************************************


class Main(object):
    @classmethod
    def cls_func(cls):
        pass

# 等价于


class Main2(object):
    def cls_func(self):
        pass
    cls_func = classmethod(cls_func)


if __name__ == '__main__':
    # countdown(10000)
    countdown.__wrapped__(10000)
    countdown = timedelta(countdown2)
    countdown(10000)
    print(countdown.__dict__)
    print(countdown.__name__)
