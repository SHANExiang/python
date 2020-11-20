

'''
Write a Python program to input two integers in a single line.
'''


def test_input_two_integers_in_single_line():
    print('input the value of x & y')
    x, y = map(int, input().split())
    print('the value of x & y are---', x, y)


# test_input_two_integers_in_single_line()
# input the value of x & y
# 12  23
# the value of x & y are--- 12 23

# ****************************************************************************
'''
Write a Python program to add three given lists using Python map and lambda.
'''


def add_three_lists():
    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7, 8]
    list3 = [9, 10, 11, 12]
    return list(map(lambda x,y,z: x + y + z, list1, list2, list3))


# print('three list add:', add_three_lists())
# three list add: [15, 18, 21, 24]

# ****************************************************************************
'''
Write a Python program to listify the list of given strings individually using Python map.
'''


def listify_list_given_strings():
    color = ['Red', 'Blue', 'Black', 'White', 'Pink']
    print('list string:', list(map(list, color)))


# listify_list_given_strings()
# list string: [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

# ****************************************************************************
'''
Write a Python program to create a list containing the power of 
said number in bases raised to the corresponding number in the index using Python map
也就是根据两个列表，求幂运算；
'''


def power():
    bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(pow, bases_num, index)))


# power()
# [10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000, 387420489000000000, 100000000000000000000]

# ****************************************************************************
'''
Write a Python program to square the elements of a list using map() function.
'''


def square_list_elements():
    original_list = [4, 5, 2, 9]
    print(list(map(lambda x: x ** 2, original_list)))


# square_list_elements()
# [16, 25, 4, 81]

# ****************************************************************************
'''
Write a Python program to convert all the characters in uppercase and lowercase 
and eliminate duplicate letters from a given sequence. Use map() function. 
将所有的字符都都转化成大写和小写，并去掉重复项；
'''


def convert_all_characters():
    characters = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

    def change_case(s):
        return s.upper(), s.lower()

    print('convert upper and lower case:', list(map(change_case, characters)))
    print('eliminate duplicate:', set(map(change_case, characters)))


# convert_all_characters()
# convert upper and lower case: [('B', 'b'), ('E', 'e'), ('U', 'u'), ('A', 'a'), ('O', 'o'), ('I', 'i'), ('F', 'f')]
# eliminate duplicate: {('E', 'e'), ('U', 'u'), ('O', 'o'), ('A', 'a'), ('F', 'f'), ('I', 'i'), ('B', 'b')}

# ****************************************************************************
'''
Write a Python program to add two given lists and find the difference between lists. 
Use map() function
'''


def find_difference():
    nums1 = [6, 5, 3, 9]
    nums2 = [0, 1, 7, 7]

    def addition_and_subtraction(x, y):
        return x + y, x - y

    print('Result:', list(map(addition_and_subtraction, nums1, nums2)))


# find_difference()
# Result: [(6, 6), (6, 4), (10, -4), (16, 2)]

# ****************************************************************************
'''
Write a Python program to convert a given list of integers 
and a tuple of integers in a list of strings. 
'''


def convert_list_integer_in_string(integers_list, integers_tuple):
    result_list = list(map(str, integers_list))
    result_tuple = tuple(map(str, integers_tuple))
    print('result_list:', result_tuple)
    print('result_tuple:', result_list)


# convert_list_integer_in_string([1, 2, 3, 4, 5], (1, 2, 3, 4, 5))
# result_list: ('1', '2', '3', '4', '5')
# result_tuple: ['1', '2', '3', '4', '5']

# ****************************************************************************
'''
Write a Python program to compute the square of first N Fibonacci numbers, 
using map function and generate a list of the numbers
'''


def square_first_n_fibonacci_numbers(n):
    import itertools

    def get_fibonacci_numbers(a=0, b=1):
        yield a
        while True:
            yield b
            a, b = b, a + b
    result = list(itertools.islice(get_fibonacci_numbers(), n))
    print('get first n fibonacci numbers:',
          list(itertools.islice(get_fibonacci_numbers(), n)))
    print(list(map(lambda x: x ** 2, result)))


square_first_n_fibonacci_numbers(5)
# get first n fibonacci numbers: [0, 1, 1, 2, 3]
# [0, 1, 1, 4, 9]


