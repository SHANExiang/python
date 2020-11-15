from collections import Counter
from itertools import zip_longest, chain, tee, groupby
from operator import itemgetter


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

# ****************************************************************************


def common_items_in_two_list():
    color1 = "Red", "Green", "Orange", "White"
    color2 = "Black", "Green", "White", "Pink"
    print(color1, color2, type(color1))
    return set(color1) & set(color2)


# print(common_items_in_two_list())
# output:
# {'Green', 'White'}
# ****************************************************************************
'''
Write a Python program to change the position of every n-th value with the (n+1)th in a list.
'''


def change_position(lis):
    for x in range(0, len(lis), 2):
        lis[x], lis[x+1] = lis[x+1], lis[x]
    return lis


# print(change_position([1, 2, 3, 4, 5, 6]))

# ****************************************************************************
'''
Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
'''


def convert_list_to_integer(lis):
    return int(''.join(map(str, lis)))


# print(convert_list_to_integer([11, 33, 4, 56]))
# output:
# 1133456

# ****************************************************************************
'''
Write a Python program to split a list based on first character of word.
意思是将一个包含str的列表中的元素按每个word的首字母区分开；
'''

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']


def split_list_by_first_character(word_list):
    # one way
    # result = dict()
    # for word in word_list:
    #     if word[0] not in result:
    #         result[word[0]] = [word]
    #     else:
    #         result[word[0]].append(word)
    # return result

    # another way
    # key使用itemgetter(0)--表示使用word的首字母，下面两行等价
    # for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    for letter, words in groupby(sorted(word_list), key=lambda x: x[0]):
        print('\n', letter)
        for word in words:
            print(word, end=',')


# print(split_list_by_first_character(list(word_list)))
# ****************************************************************************


# print([[5 * x + res for res in range(1, 6)] for x in range(0, 5)])

'''
Write a Python program to insert an element before each element of a list.
list中每个元素前insert一个元素；
'''


def insert_element(element, lis):
    # one way
    # result_list = list()
    # for x in lis:
    #     result_list.append(element)
    #     result_list.append(x)
    # return result_list

    # another way
    return [v for ele in lis for v in (element, ele)]


# print(insert_element(5, [1, 2, 3, 4]))
# result = list()
# for ele in [1, 2, 3, 4]:
#     for v in (5, ele):
#         result.append(v)

# ****************************************************************************
'''
Write a Python program to split a list every Nth element. Go to the editor
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
'''
original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


def split_list_nth_element(original_list, step):
    # one way
    # result_list = list()
    # for x in range(step):
    #     init_list = list()
    #     for y in range((len(original_list) // step) + 1):
    #         if x + step * y < len(original_list):
    #             init_list.append(original_list[x + step * y])
    #     result_list.append(init_list)
    # return result_list

    # another way
    return [original_list[x::step] for x in range(step)]


# print(split_list_nth_element(original_list, 3))
# ****************************************************************************
'''
Write a Python program to compute the difference between two lists.
'''


def compute_difference_two_list(list1, list2):
    # use collections.Counter
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    print(counter1 - counter2) # Counter({'red': 1, 'orange': 1, 'white': 1})
    print(list({'red': 1, 'orange': 1, 'white': 1}))  # ['red', 'orange', 'white']
    return list(counter1 - counter2), list(counter2 - counter1)


color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
# print(compute_difference_two_list(color1, color2))
# (['red', 'orange', 'white'], ['black', 'yellow'])

# ****************************************************************************
'''
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''


def replace_last_element(original_list, target_list):
    original_list[-1:] = target_list
    return original_list


# print(replace_last_element([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
# [1, 3, 5, 7, 9, 2, 4, 6, 8]

# lis = [(4, 1), (1, 2), (6, 0)]
# print(min(lis, key=lambda x: x[1]))
# print([40, 50, 60] + [10, 20, 30])

# ****************************************************************************
'''
 Write a Python program to remove duplicates from a list of lists. 
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''


# 将一个内嵌的list，转换成单元素并且未有重复元素的list
def get_union_list(original_list):
    return list(set().union(*original_list))


# print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
# [33, 40, 10, 20, 56, 25, 30]


def remove_duplicates(original_list):
    original_list.sort()
    new_list = list(num for num, _ in groupby(original_list))
    return new_list


# print(remove_duplicates([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
# [[10, 20], [30, 56, 25], [33], [40]]

# ****************************************************************************
'''
Write a Python program to get the depth of a dictionary.
'''


def get_depth_dictionary(d):
    if isinstance(d, dict):
        return 1 + (max(map(get_depth_dictionary, d.values())) if d else 0)
    return 0


# print(get_depth_dictionary({'a':1, 'b': {'c': {'d': {}}}}))
# ****************************************************************************
'''
Write a Python program to check whether all dictionaries in a list are empty or not. 
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
'''


def whether_all_dict_empty(original_list):
    flag = False
    for d in original_list:
        if isinstance(d, dict) and not d:
            flag = True
        else:
            flag = False
    return flag


print(whether_all_dict_empty([{1, 2}, {}, {}]))
