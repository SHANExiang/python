l = [1, 2, 3, 4, 10]
t =(2, 4, 8, 11, 15)

s1 = set(l)
s2 = set(t)
# print('s1==%s' % s1, 's2==%s' % s2, sep='\n', end='dong\n')
# 相同的元素
# print(s1 - s2) # s1中有s2中没有的元素
# print(s1 + s2)# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(s2 - s1) # s2中有s1中没有的元素
# print(s1 & s2) # {2, 4}   s1与s2的交集
# print(s1 ^ s2) # {1, 3, 8, 10, 11, 15}  两者总和去掉交集元素
# print(s1.union(s2))


def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  print(n)
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n


# print(absent_digits([9,8,3,2,2,0,9,7,6,3]))


# ****************************************************************************
'''
Write a Python program to check if a set is a subset of another set. 
'''


def is_subset(set1, set2):
    return set2.issubset(set1)


# print(is_subset(set(['apple', 'orange']), set(['orange'])))
# True
'''
Write a Python program to use of frozensets.
Note: Frozensets behave just like sets except they are immutable.
'''


def test_frozenset():
    set1 = set(['a', 'b', 'c', 'd'])
    set2 = set(['c', 'd', 'e', 'f'])
    x = frozenset([1, 2, 3, 4, 5])
    y = frozenset([3, 4, 5, 6, 7])
    # print(x.isdisjoint(y)) # Return True if two sets have a null intersection
    # print(set1.isdisjoint(set2))
    # print(x.difference(y))
    # print(x | y)


test_frozenset()
# False
# False
# frozenset({1, 2})
# frozenset({1, 2, 3, 4, 5, 6, 7})
# ****************************************************************************
'''
Write a Python program to remove the intersection of a 2nd set from the 1st set.
从第一个集合中移除两个集合的交集；
'''


def remove_intersection():
    set1 = set([1, 2, 3, 4, 5])
    set2 = set([4, 5, 6, 7, 8])
    set1.difference_update(set2)
    print(set1)
    print(set2)


remove_intersection()
# {1, 2, 3}
# {4, 5, 6, 7, 8}
