# list类的sort方法进行排序，且还是原列表的顺序
lis1 = [1, 2, 3, 4, 2, 7, 3]
lis2 = list(set(lis1))
lis2.sort(key=lis1.index)
# print(lis2)
# [1, 2, 3, 4, 7]
# 使用sorted函数
# print(sorted(lis2, key=lis1.index))

# 遍历进行排序
lis3 = list()
for x in lis1:
    if x not in lis3:
        lis3.append(x)
# print(lis3)


# Write a Python program to remove the first item from a specified list.
def remove_first_item_from_specified_list():
    color = ["Red", "Black", "Green", "White", "Orange"]
    print("\nOriginal Color: ",color)
    del color[0]
    print("After removing the first color: ", color)
    color.pop(0)
    print("After pop the first color: ", color)


# remove_first_item_from_specified_list()
# Original Color:  ['Red', 'Black', 'Green', 'White', 'Orange']
# After removing the first color:  ['Black', 'Green', 'White', 'Orange']
# After pop the first color:  ['Green', 'White', 'Orange']


# ****************************************************************************
import builtins
# print(builtins.__dict__, len(builtins.__dict__), sep='\n')


# ****************************************************************************
'''
Write a Python program to create a bytearray from a list.
'''


def test_list_to_bytearray():
    lis = [34, 36, 29, 10]
    array = bytearray(lis)
    for x in array:
        print(x, end='\n')

# test_list_to_bytearray()
# 34
# 36
# 29
# 10


'''
Write a Python program to split a variable length string into variables.
'''


def test_split_a_variable_length_string_into_variables():
   lis = ['a', 'b', 'c']
   lis1 = lis + [None]*3
   print(lis1, len(lis1)) # ['a', 'b', 'c', None, None, None] 6
   x, y, z = lis1[:3]
   print(x, y, z, type(x))
   var_list = [100, 20.25]
   x, y = (var_list + [None] * 2)[:2]
   print(x, y)


# test_split_a_variable_length_string_into_variables()
# ['a', 'b', 'c', None, None, None] 6
# a b c <class 'str'>
# 100 20.25


'''
Write a Python program to remove and print every third number from a list of
 numbers until the list becomes empty.
'''


def test_remove_every_third_number():
    lis = [23, 25, 1, 123, 90, 56]
    position = 3 - 1
    index = 0
    len_lis = len(lis)
    while len_lis > 0:
        index = (position + index) % len_lis
        print(lis.pop(index))
        len_lis -= 1


# test_remove_every_third_number()
# 1
# 56
# 123
# 25
# 90
# 23

# ****************************************************************************
nums = [2, 3, 4, 5]


def test_create_permutations(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms


# print(test_create_permutations(nums))
# [[5, 4, 3, 2], [4, 5, 3, 2], [4, 3, 5, 2], [4, 3, 2, 5], [5, 3, 4, 2],
# [3, 5, 4, 2], [3, 4, 5, 2], [3, 4, 2, 5], [5, 3, 2, 4], [3, 5, 2, 4],
# [3, 2, 5, 4], [3, 2, 4, 5], [5, 4, 2, 3], [4, 5, 2, 3], [4, 2, 5, 3],
# [4, 2, 3, 5], [5, 2, 4, 3], [2, 5, 4, 3], [2, 4, 5, 3], [2, 4, 3, 5],
# [5, 2, 3, 4], [2, 5, 3, 4], [2, 3, 5, 4], [2, 3, 4, 5]]

# ****************************************************************************
string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}


def get_letter_combinations1(digit_str):
    result = []
    a = digit_str[0]
    b = digit_str[1]
    if a in string_maps and b in string_maps:
        a_map = string_maps.get(a)
        b_map = string_maps.get(b)
        import itertools
        for x in itertools.product(a_map, b_map):
            result.append(x[0] + x[1])
    return result


def get_letter_combinations2(digit_str):
    result = [""]
    for x in digit_str:
        temp = []
        for s in result:
            for char in string_maps[x]:
                temp.append(s + char)
        result = temp
    return result


# print(get_letter_combinations1("34"))
# print(get_letter_combinations2('56'))
# ['gj', 'gk', 'gl', 'hj', 'hk', 'hl', 'ij', 'ik', 'il']
# ['mp', 'mq', 'mr', 'ms', 'np', 'nq', 'nr', 'ns', 'op', 'oq', 'or', 'os']
