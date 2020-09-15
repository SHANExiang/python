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


test_split_a_variable_length_string_into_variables()
# ['a', 'b', 'c', None, None, None] 6
# a b c <class 'str'>
# 100 20.25
