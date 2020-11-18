import collections
import pprint


# Write a Python program to count the number of each character of a text file.
file_path = input('file is --')
with open(file_path, 'r') as info:
    count = collections.Counter(info.read().upper())
    print(count.items())
    pprint.pprint(count)


# file is --abc.txt
# dict_items([('G', 13), ('E', 64), ('R', 29), ('M', 17), ('A', 42), ('N', 45), (' ', 86), ('U', 14), ('I', 36), ('T', 40), ('Y', 17), ('D', 19), ('\n', 10), ('F', 15), ('O', 31), ('W', 5), ('K', 1), ('P', 4), (',', 7), ('H', 25), ('C', 13), ('L', 15), ('(', 1), (':', 1), ('S', 12), (')', 1), ('B', 6), ('3', 2), ('.', 4), ('V', 1), ('1', 3), ('9', 5), ('0', 2), ('-', 1)])
# Counter({' ': 86,
#          'E': 64,
#          'N': 45,
#          'A': 42,
#          'T': 40,
#          'I': 36,
#          'O': 31,
#          'R': 29,
#          'H': 25,
#          'D': 19,
#          'M': 17,
#          'Y': 17,
#          'F': 15,
#          'L': 15,
#          'U': 14,
#          'G': 13,
#          'C': 13,
#          'S': 12,
#          '\n': 10,
#          ',': 7,
#          'B': 6,
#          'W': 5,
#          '9': 5,
#          'P': 4,
#          '.': 4,
#          '1': 3,
#          '3': 2,
#          '0': 2,
#          'K': 1,
#          '(': 1,
#          ':': 1,
#          ')': 1,
#          'V': 1,
#          '-': 1})

# ****************************************************************************
def test_sum_numbers_counts():
    num = [2, 3, 4, 3, 3, 0, 10, 4, 4, 4]
    c = collections.Counter(num)
    print(c, c.items(), type(c.items()))
    print(sum(c.values())) # 求数字出现次数的和


test_sum_numbers_counts()
# Counter({4: 4, 3: 3, 2: 1, 0: 1, 10: 1})
# dict_items([(2, 1), (3, 3), (4, 4), (0, 1), (10, 1)]) <class 'dict_items'>
# 10

# ****************************************************************************

