

# Write a Python program to get numbers divisible by fifteen from a list
# using an anonymous function
def test_division_5_in_list(lis):
    return list(filter(lambda x : x % 5 == 0, lis))


# print(test_division_5_in_list([35, 25, 20, 71, 55]))
# [35, 25, 20, 55]


'''
Write a Python program to extract year, month, date and time using Lambda
'''


def extract_date():
    import datetime
    now = datetime.datetime.now()
    print(now)
    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    time = lambda x: x.time()
    print('year==%s' % year(now))
    print('month==%s' % month(now))
    print('day==%s' % day(now))
    print('time==%s' % time(now))


# extract_date()
# 2020-11-20 20:06:57.371034
# year==2020
# month==11
# day==20
# time==20:06:57.371034

'''
Write a Python program to create Fibonacci series upto n using Lambda.
'''


def create_fibonacci_series(n):
    import functools
    return functools.reduce(lambda x, _: x + [x[-1] + x[-2]],
                            range(n - 2), [0, 1])


# print(create_fibonacci_series(6))
# [0, 1, 1, 2, 3, 5]

# ****************************************************************************
'''
Write a Python program to find intersection of two given arrays using Lambda.
'''


def find_intersection():
    array1 = [2, 3, 4, 5, 6]
    array2 = [1, 2, 3, 4, 5]
    return list(filter(lambda x: x in array1, array2))


# print(find_intersection())
# [2, 3, 4, 5]

# ****************************************************************************
'''
Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
'''


def sort_positive_negative_nums():
    array_nums = [-1, 2, -3, 5, 7, 8, 9, -10, 0]
    return sorted(array_nums,key=lambda x: 1 if x == 0 else -1 / x)


print(sort_positive_negative_nums())
# [2, 5, 7, 8, 9, 0, -10, -3, -1]
