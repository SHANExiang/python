from functools import wraps


class Decorate(object):
    def decorate1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate1, instance method')
            func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorate2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate2, classmethod')
            func(*args, **kwargs)
        return wrapper


d = Decorate()


@d.decorate1
def add(x, y):
    print('add')
    return x + y


@Decorate.decorate2
def spam():
    print('spam')


if __name__ == '__main__':
    add(2, 4)
    spam()
