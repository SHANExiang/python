from functools import wraps
import time


def timedelta(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('use time', (end_time - start_time))
        return result
    return wrapper


class Test(object):
    @timedelta
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timedelta
    def class_method(cls, n):
        print(cls, n)
        while n> 0:
            n -= 1

    @staticmethod
    @timedelta
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


if __name__ == '__main__':
    test = Test()
    test.instance_method(10000)
    test.static_method(10000)
    test.class_method(10000)


