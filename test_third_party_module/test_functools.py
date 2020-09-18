import itertools
from functools import partial


def check_sum_array(T, *nums):
    if sum(x for x in nums) == T:
        return True, nums
    else:
        return False, nums


# x = [10, 20, 20, 20]
# y = [10, 20, 30, 40]
# z = [10, 30, 40, 20]
# T = 70
# for x in itertools.product(x, y, z):
#     print(x)
#
# pro = itertools.product(x, y, z)
# func = partial(check_sum_array, T)
# print(func(10, 20, 30))
# print(list(itertools.starmap(func, pro)))


def test_sum_three_element_from_three_array_equal_target():
    x = [10, 20, 20, 20]
    y = [10, 20, 30, 40]
    z = [10, 30, 40, 20]
    T = 70
    pro = itertools.product(x, y, z) # 产生所有组合
    func = partial(check_sum_array, T) # 先将target value摘出来
    sums = list(itertools.starmap(func, pro))
    result = set()
    for r in sums:
        if r[0] == True and r[1] not in result:
            result.add(r[1])
            print(result)


# test_sum_three_element_from_three_array_equal_target()
# {(10, 20, 40)}
# {(10, 30, 30), (10, 20, 40)}
# {(10, 30, 30), (10, 20, 40), (10, 40, 20)}
# {(10, 30, 30), (20, 10, 40), (10, 20, 40), (10, 40, 20)}
# {(10, 20, 40), (20, 20, 30), (20, 10, 40), (10, 40, 20), (10, 30, 30)}
# {(10, 20, 40), (20, 20, 30), (20, 10, 40), (10, 40, 20), (20, 30, 20), (10, 30, 30)}
# {(10, 20, 40), (20, 40, 10), (20, 20, 30), (20, 10, 40), (10, 40, 20), (20, 30, 20), (10, 30, 30)}


def test_itertools_product():
    pro1 = itertools.product('34', '23')
    for x in pro1:
        print(x)
    print('pro2=================================')
    pro2 = itertools.product('34', '23', repeat=2)
    for x in pro2:
        print(x)
    print('pro3=================================pro2与pro3等价')
    pro3 = itertools.product('34', '23', '34', '23')
    for x in pro3:
        print(x)


# test_itertools_product()
# ('3', '2')
# ('3', '3')
# ('4', '2')
# ('4', '3')
# pro2=================================
# ('3', '2', '3', '2')
# ('3', '2', '3', '3')
# ('3', '2', '4', '2')
# ('3', '2', '4', '3')
# ('3', '3', '3', '2')
# ('3', '3', '3', '3')
# ('3', '3', '4', '2')
# ('3', '3', '4', '3')
# ('4', '2', '3', '2')
# ('4', '2', '3', '3')
# ('4', '2', '4', '2')
# ('4', '2', '4', '3')
# ('4', '3', '3', '2')
# ('4', '3', '3', '3')
# ('4', '3', '4', '2')
# ('4', '3', '4', '3')
# pro3=================================pro2与pro3等价
# ('3', '2', '3', '2')
# ('3', '2', '3', '3')
# ('3', '2', '4', '2')
# ('3', '2', '4', '3')
# ('3', '3', '3', '2')
# ('3', '3', '3', '3')
# ('3', '3', '4', '2')
# ('3', '3', '4', '3')
# ('4', '2', '3', '2')
# ('4', '2', '3', '3')
# ('4', '2', '4', '2')
# ('4', '2', '4', '3')
# ('4', '3', '3', '2')
# ('4', '3', '3', '3')
# ('4', '3', '4', '2')
# ('4', '3', '4', '3')


def test_itertools_starmap():
    map = itertools.starmap(str.isdigit, '34dfgg43dfd')
    print('type(map)==%s', type(map))
    print(list(map))


test_itertools_starmap()
# type(map)==%s <class 'itertools.starmap'>
# [True, True, False, False, False, False, True, True, False, False, False]
