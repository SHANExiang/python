

class Foo(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        n = self.x
        self.x += 1
        return self.x


foo = Foo(3)
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
# for x in foo:
#     print(x)
