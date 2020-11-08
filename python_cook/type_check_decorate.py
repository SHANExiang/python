from functools import wraps
from inspect import signature


def type_assert(*type_args, **type_kwargs):
    def decorate(func):
        sig = signature(func)
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments
        print(bound_types)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            "Argument {} must be {}".format(
                                name,bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate


@type_assert(int, int)
def add(x, y):
    return x + y


if __name__ == '__main__':
    sig = signature(add)
    print(sig.bind_partial())
