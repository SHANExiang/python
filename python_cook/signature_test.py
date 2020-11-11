from inspect import Signature, Parameter
import inspect


params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=24),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]

sig = Signature(params)
# print(sig)  # (x, y=24, *, z=None)


def func(*args, **kwargs):
    bound_args = sig.bind(*args, **kwargs)
    for key, value in bound_args.arguments.items():
        print(key, value)


# ****************************************************************************


def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(params)


class Structure(object):
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_args = self.__signature__.bind(*args, **kwargs)
        for key, value in bound_args.arguments.items():
            setattr(self, key, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


if __name__ == '__main__':
    # func(1, 2, z=3)

    print(inspect.signature(Stock)) # (name, shares, price)
    s1 = Stock('dong', 10, 21.1) # 正常创建
    s2 = Stock('dong', 10)  # missing a required argument: 'price'
