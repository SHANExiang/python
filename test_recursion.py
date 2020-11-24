

"""
Write a Python program to calculate the sum of a list of numbers.
"""


def sum_list(original_list):
    if len(original_list) == 1:
        return original_list[0]
    else:
        return original_list[0] + sum_list(original_list[1:])


# print(sum_list([1, 2, 3, 5, 10]))
# 21

# ****************************************************************************
'''
Write a Python program to converting an Integer to a string in any base.
'''


def convert_to_list(original_int):
    # 数字转为str
    if 0 < original_int < 10:
        return str(original_int)
    else:
        return convert_to_list(original_int//10) + \
               convert_to_list(original_int%10)


# print(type(convert_to_list(1122)), convert_to_list(1122))


def convert_list_in_base(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    else:
        return convert_list_in_base(num//base, base) + \
               convert_string[num%base]


# print(convert_list_in_base(3456, 13))
# 175B


# ****************************************************************************
'''
Write a Python program of recursion list sum. 
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21
'''


def list_sum_list(original_list):
    sum = 0
    for x in original_list:
        if isinstance(x, int):
            sum += x
        if isinstance(x, list):
            sum += list_sum_list(x)
    return sum


# print(list_sum_list([1, 2, [3,4], [5,6]]))
# 21


# ****************************************************************************
'''
Write a Python program to get the factorial of a non-negative integer
'''


def get_factorial(num):
    if num == 1:
        return 1
    else:
        return num*get_factorial(num - 1)


# print(get_factorial(6))
# 720

# ****************************************************************************
'''
Write a Python program to solve the Fibonacci sequence using recursion.
'''


def solve_fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    return solve_fibonacci_sequence(n - 1) + solve_fibonacci_sequence(n - 2)


# print(solve_fibonacci_sequence(7))
# 13


'''
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). 
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
'''


def sum_series(n):
    if n == 1 or n == 0:
        return n
    return n + sum_series(n - 2)


# print(sum_series(6)) # 12
# print(sum_series(10)) # 30

"""
Write a Python program to calculate the harmonic sum of n-1. Go to the editor
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series--1 + 1/2 + 1/3 + 1/4 ... 
"""


def harmonic_sum(n):
    if n == 1:
        return 1
    return 1/n + harmonic_sum(n - 1)


# print(harmonic_sum(7))
# 2.5928571428571425

'''
Write a Python program to find the greatest common divisor (gcd) of two integers
'''


def get_gcd(x, y):
    low = min(x, y)
    high = max(x, y)
    if low == 0:
        return high
    if low == 1:
        return 1
    else:
        return get_gcd(low, high%low)


print(get_gcd(12, 24))
