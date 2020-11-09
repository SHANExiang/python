from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if not debug:
            print('calling:', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def spam(x, y, z):
    print(x, y, z)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(2, 3, 4, debug=True)
