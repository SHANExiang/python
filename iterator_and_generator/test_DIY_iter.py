

class Foo(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        n = self.x
        self.x += 1
        return n


# 执行代码
# foo = Foo(3)
# for x in foo:
#     if x < 10:
#         print(x)
#     else:
#         break

# output:
# 3
# 4
# 5
# 6
# 7
# 8
# 9

class Foo1(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        num = self.start
        if self.start == self.end:
            raise StopIteration
        self.start += 1
        return num


# 执行代码
# foo1 = Foo1(1, 4)
# for x in foo1:
#     print(x)

# output:
# 1
# 2
# 3
