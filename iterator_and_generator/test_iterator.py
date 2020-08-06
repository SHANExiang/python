from collections.abc import Iterable, Iterator


f = open('test.txt', 'r')
a = 10
b = 'dong'
c = {'name': 'dong'}
d = ['2', 3, '56', 'ssha']
e = (2, 3, (3, 4, 6), 'sa')
g = {2, 4, 9, 10}


# 判断对象是否是可迭代的
print(isinstance(f, Iterable)) # True
print(isinstance(a, Iterable)) # False
print(isinstance(b, Iterable)) # True
print(isinstance(c, Iterable)) # True
print(isinstance(d, Iterable)) # True
print(isinstance(e, Iterable)) # True
print(isinstance(g, Iterable), '\n') # True


# 可迭代表明有__iter__方法
print(hasattr(f, '__iter__')) # True
print(hasattr(a, '__iter__')) # False
print(hasattr(b, '__iter__')) # True
print(hasattr(c, '__iter__')) # True
print(hasattr(d, '__iter__')) # True
print(hasattr(e, '__iter__')) # True
print(hasattr(g, '__iter__'), '\n') # True


# 迭代器与可迭代对象的区别就是，迭代器中多个__next__方法
print(isinstance(f, Iterator)) # True
print(isinstance(a, Iterator)) # False
print(isinstance(b, Iterator)) # False
print(isinstance(c, Iterator)) # False
print(isinstance(d, Iterator)) # False
print(isinstance(e, Iterator)) # False
print(isinstance(g, Iterator), '\n') # False


print(hasattr(f, '__next__')) # True
print(hasattr(a, '__next__')) # False
print(hasattr(b, '__next__')) # False
print(hasattr(c, '__next__')) # False
print(hasattr(d, '__next__')) # False
print(hasattr(e, '__next__')) # False
print(hasattr(g, '__next__'), '\n') # False

########################################################################
l = [1, 2, 3, 4, 5]
for i in l:
    print(i, '\n')


it = l.__iter__()
print(type(it)) # <class 'list_iterator'>
print(it.__next__()) # 1
print(it.__next__()) # 2
print(it.__next__()) # 3
print(it.__next__()) # 4
print(it.__next__()) # 5
print(it.__next__()) # 什么都不输出

########################################################################

M = ['a', 'b', 'c', 'd', 'e']
for x in M:  # 解释器隐式调用
    print(x)

for x in iter(M):  # 等价于 M.__iter()__   人为显示调用
    print(x)
