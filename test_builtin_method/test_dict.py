from collections import Counter, defaultdict
from itertools import product, groupby
from operator import itemgetter
import uuid


# 合并两个字典
# 第一种方式
x = {'name': 'dong', 'age': 10}
y = {'host': 'compute', 'id': uuid.uuid4()}

# z = x.copy()
# print('z==%s' % z, 'id(x)==%s' % id(x), 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10} id(x)==2342080434368 id(z)==2342110319872
# z.update(y)
# print('z==%s' % z, 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10, 'host': 'compute',
# 'id': UUID('e4379eb9-5d36-4018-baf6-b6d0b0572441')} id(z)==2689673090240
# update()是就地和并字典，z还是同样的内存地址

# 第二种方式，python3.5以上版本
# z = {**x, **y}
# print('z==%s' % z, 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10, 'host': 'compute',
# 'id': UUID('2f06eb3b-b1f2-4b4b-9321-4a42f5b5f2d5')} id(z)==1376163448128
# z又存储到另一块内存

# 遍历字典两种方式
dic = {'name': 'dong', 'age': 20, 'gender': (0, 1)}
# for k in dic:
#     print('key==%s, value==%s' % (k, dic[k]))

# key==name, value==dong
# key==age, value==20
# key==gender, value==(0, 1)

# for key, value in dic.items():
#     print('key==%s, value==%s' % (key, value))

# 判断字典中是否有某一key
# print('name' in dic) # True
# print('ag' not in dic) # True


# 根据字典value进行排序 x[0]表示键,x[1]表示值
d = {'354': 34, 'dong': 54, 'fh': 10}
# print(sorted(d.items(), key=lambda x:x[1]))
# [('fh', 10), ('354', 34), ('dong', 54)]

# 将字符串转变成字典
str1 = "k:1|k1:2|k2:3|k3:4"
# dict1 = dict()
# for x in str1.split("|"):
#     y = x.split(":")
#     print(y)
#     print('key==%s, value==%s' % (y[0], y[1]))
#     dict1.update({'%s' % y[0]: y[1]})
#     print(dict1)

# ['k', '1']
# key==k, value==1
# {'k': '1'}
# ['k1', '2']
# key==k1, value==2
# {'k': '1', 'k1': '2'}
# ['k2', '3']
# key==k2, value==3
# {'k': '1', 'k1': '2', 'k2': '3'}
# ['k3', '4']
# key==k3, value==4
# {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}

# 公差为11的等差数列
# print([x * 11 for x in range(10)])

# 字典和集合解析
my_dict = {i: i * i for i in range(10)}
my_set = {i * i for i in range(10)}
# print('dict==%s, set==%s' % (my_dict, my_set))
# dict=={0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81},
# set=={0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# ****************************************************************************
'''
Write a Python program to extract single key-value pair of a dictionary in variables.
'''


def test_items():
    dic11 = {'name': 'dong123'}
    (x, y), = dic11.items()
    print(x, y)


# test_items()
# name dong123
# ****************************************************************************
'''
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''


def create_combinations_of_letters(original_dict):
    for x in product(*[original_dict[key] for key in sorted(original_dict.keys())]):
        print(''.join(x))


# create_combinations_of_letters({'1': ['a', 'b'], '2': ['c', 'd']})
# ac
# ad
# bc
# bd
# ****************************************************************************
'''
Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
'''


def combine_value_dictionary(original_list):
    result = Counter()
    for x in original_list:
        result[x['item']] += x['amount']
    return result


# print(combine_value_dictionary(
#     [{'item': 'item1', 'amount': 400},
#      {'item': 'item2', 'amount': 300},
#      {'item': 'item1', 'amount': 750}]))
# ****************************************************************************
'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
'''


def create_dict_from_str(string):
    print(dict(Counter(string)))


# create_dict_from_str("w3resource")
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# ****************************************************************************
'''
Write a Python program to print a dictionary in table format.
'''


def print_in_table_format(original_dict):
    for row in zip(*([key] + (value)
                     for key, value in sorted(original_dict.items()))):
        print(*row)


# print_in_table_format({'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]})
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11


dict1 = defaultdict(set)
dict2 = defaultdict(int)
dict3 = defaultdict(str)
dict4 = defaultdict(list)

# print(dict1[1])
# print(dict2[1])
# print(dict3[1])
# print(dict4[1])
# set()
# 0
#
# []

test_dict1 = {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82}
# print(test_dict1.pop('id'))  # 1
# print(test_dict1) # {'subject': 'math', 'V': 70, 'VI': 82}


test_dict2 = {'key1': 1, 'key2': 3, 'key3': 2}
test_dict3 = {'key1': 1, 'key2': 2}
# print(set(test_dict2.items()))  # {('key1', 1), ('key3', 2), ('key2', 3)}
# print(set(test_dict3.items()))  # {('key1', 1), ('key2', 2)}
# print(set(test_dict2.items()) & set(test_dict3.items()))

