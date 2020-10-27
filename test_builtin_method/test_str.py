

# Write a Python program to count the number of occurrence of a specific character in a string.
def test_count():
    s = 'The quick brown fox jumps over the lazy dog.'
    print('the occurrence times of character %s is %s' % ('e', s.count('e')))


# test_count()
# the occurrence times of character e is 3


# Write a Python program to check whether a string is numeric.
def test_string_whether_numeric():
    st = 'sd234'
    try:
        num = float(st)
    except (ValueError, TypeError):
        print('not numeric')


# test_string_whether_numeric()
# not numeric

# Write a Python program to convert a byte string to a list of integers.
def test_string_convert_integer_list():
    by = b'ABm'
    print(list(by))

# test_string_convert_integer_list()
# [65, 66, 109]


'''
Write a Python program to print Unicode characters. 
'''
# print(u'\u0050\u0079\u0074\u0068\u006f\u006e')  # Python  打印unicode字符


'''
Write a Python program to prove that two string variables of same value
 point same memory location.
'''
st1 = 'dong'
st2 = 'dong'
# print('st1的内存地址==%s\nst2的内存地址==%s' % (hex(id(st1)), hex(id(st2))))
# st1的内存地址==0x2062aafc930
# st2的内存地址==0x2062aafc930


'''
Write a Python program to add trailing and leading zeroes to a string
'''


def test_add_trailing_and_leading_zeroes_to_a_string():
    st = 'dgfr45sfry4'
    print('origin string---%s, len(st)---%s' % (st, len(st)))
    st1 = st.ljust(15, '0')
    print('add trailing zeroes---', st1)
    st2 = st.ljust(15, '*')
    print('add trailing *---', st2)
    st3 = st.rjust(15, '0')
    print('add leading zeroes---', st3)
    st4 = st.rjust(15, '*')
    print('add leading zeroes---', st4)


# test_add_trailing_and_leading_zeroes_to_a_string()
# origin string---dgfr45sfry4, len(st)---11
# add trailing zeroes--- dgfr45sfry40000
# add trailing *--- dgfr45sfry4****
# add leading zeroes--- 0000dgfr45sfry4
# add leading zeroes--- ****dgfr45sfry4


# print('\"sdogong\"')


'''
Write a Python program to create the combinations of 3 digit combo.
'''


def test_combination_3_digit():
    nums = []
    for x in range(15):
        num = str(x).zfill(3)
        nums.append(num)
    return nums


# print(test_combination_3_digit())


'''
Write a Python program to print a long text, convert the string to a list and 
print all the words and their frequencies.
'''
text = '''
    We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
    Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.
    
    This has been called "one of the best-known sentences in the English language", containing "the most potent
    and consequential words in American history". The passage came to represent a moral standard to which
    the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
    Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
    through which the United States Constitution should be interpreted.
    '''


def test_get_freq():
    words_list = text.split()
    word_freq = [words_list.count(x) for x in words_list]
    print('list:\n{}'.format(str(words_list)))
    print('pairs:\n{}'.format(str(list(zip(words_list, word_freq)))))


# test_get_freq()
# list:
# ['We', 'hold', 'these', 'truths', 'to', 'be', 'self-evident,', 'that',
# 'all', 'men', 'are', 'created', 'equal,', 'that', 'they', 'are', 'endowed',
# 'by', 'their', 'Creator', 'with', 'certain', 'unalienable', 'Rights,',
# 'that', 'among', 'these', 'are', 'Life,', 'Liberty', 'and', 'the',
# 'pursuit', 'of', 'Happiness.', 'This', 'has', 'been', 'called', '"one',
# 'of', 'the', 'best-known', 'sentences', 'in', 'the', 'English',
# 'language",', 'containing', '"the', 'most', 'potent', 'and',
# 'consequential', 'words', 'in', 'American', 'history".', 'The', 'passage',
# 'came', 'to', 'represent', 'a', 'moral', 'standard', 'to', 'which', 'the',
# 'United', 'States', 'should', 'strive.', 'This', 'view', 'was', 'notably',
# 'promoted', 'by', 'Abraham', 'Lincoln,', 'who', 'considered', 'the',
# 'Declaration', 'to', 'be', 'the', 'foundation', 'of', 'his', 'political',
# 'philosophy', 'and', 'argued', 'that', 'it', 'is', 'a', 'statement', 'of',
# 'principles', 'through', 'which', 'the', 'United', 'States', 'Constitution',
# 'should', 'be', 'interpreted.']
# pairs:
# [('We', 1), ('hold', 1), ('these', 2), ('truths', 1), ('to', 4), ('be', 3),
# ('self-evident,', 1), ('that', 4), ('all', 1), ('men', 1), ('are', 3),
# ('created', 1), ('equal,', 1), ('that', 4), ('they', 1), ('are', 3),
# ('endowed', 1), ('by', 2), ('their', 1), ('Creator', 1), ('with', 1),
# ('certain', 1), ('unalienable', 1), ('Rights,', 1), ('that', 4),
# ('among', 1), ('these', 2), ('are', 3), ('Life,', 1), ('Liberty', 1),
# ('and', 3), ('the', 7), ('pursuit', 1), ('of', 4), ('Happiness.', 1),
# ('This', 2), ('has', 1), ('been', 1), ('called', 1), ('"one', 1), ('of', 4),
# ('the', 7), ('best-known', 1), ('sentences', 1), ('in', 2), ('the', 7),
# ('English', 1), ('language",', 1), ('containing', 1), ('"the', 1),
# ('most', 1), ('potent', 1), ('and', 3), ('consequential', 1), ('words', 1),
# ('in', 2), ('American', 1), ('history".', 1), ('The', 1), ('passage', 1),
# ('came', 1), ('to', 4), ('represent', 1), ('a', 2), ('moral', 1),
# ('standard', 1), ('to', 4), ('which', 2), ('the', 7), ('United', 2),
# ('States', 2), ('should', 2), ('strive.', 1), ('This', 2), ('view', 1),
# ('was', 1), ('notably', 1), ('promoted', 1), ('by', 2), ('Abraham', 1),
# ('Lincoln,', 1), ('who', 1), ('considered', 1), ('the', 7),
# ('Declaration', 1), ('to', 4), ('be', 3), ('the', 7), ('foundation', 1),
# ('of', 4), ('his', 1), ('political', 1), ('philosophy', 1), ('and', 3),
# ('argued', 1), ('that', 4), ('it', 1), ('is', 1), ('a', 2),
# ('statement', 1), ('of', 4), ('principles', 1), ('through', 1),
# ('which', 2), ('the', 7), ('United', 2), ('States', 2), ('Constitution', 1),
# ('should', 2), ('be', 3), ('interpreted.', 1)]

# ****************************************************************************

# 获取n位的数字列表，它们旋转180度还是原来的值
def test_get_all_strobogrammatic_numbers_length_n(n, length):
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1', '8']
    middle = test_get_all_strobogrammatic_numbers_length_n(n - 2, length)
    result = []
    for x in middle:
        if n != length:
            result.append("0" + x + "")
        result.append('8' + x + '8')
        result.append('1' + x + '1')
        result.append('9' + x + '6')
        result.append('6' + x + '9')
    return result


# print(test_get_all_strobogrammatic_numbers_length_n(4, 4))
# ['808', '101', '906', '609', '8888', '1881', '9886', '6889', '8118',
# '1111', '9116', '6119', '8968', '1961', '9966', '6969', '8698', '1691',
# '9696', '6699']

# ****************************************************************************

#  n degrees of number 2 are written sequentially in a line without spaces.
def test_get_degrees_number2_written_sequentially_in_line_no_spaces(n):
    if n == 1:
        return '2'
    degrees_number_2 = str(pow(2, n))
    res = test_get_degrees_number2_written_sequentially_in_line_no_spaces(n-1)
    return res + degrees_number_2


# print(test_get_degrees_number2_written_sequentially_in_line_no_spaces(7))

#  find the value of n where n degrees of number 2 are written sequentially
#  in a line without spaces.
def test_get_n_from_degrees_number2_written_sequentially_in_line_no_spaces(ns):
    if ns == '2':
        return 1
    flag = True
    n, temp, i = 2, 2, 2
    while flag:
        if str(temp) in ns:
            i += 1
            temp = pow(n, i)
        else:
            flag = False
    return i - 1


# print(test_get_n_from_degrees_number2_written_sequentially_in_line_no_spaces('2481632'))


# *****************************************************************************
'''
Write a Python program to count the number of characters (character frequency) in a string.
'''


def get_number_of_characters_in_string(st):
    res = dict()
    for ch in st:
        if ch not in res:
            res[ch] = 1
        else:
            res[ch] += 1
    return res


# print(get_number_of_characters_in_string('dongdgfdsdergrh'))
# output:
# {'d': 4, 'o': 1, 'n': 1, 'g': 3, 'f': 1, 's': 1, 'e': 1, 'r': 2, 'h': 1}

# *****************************************************************************
'''
 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
 If the string length is less than 2, return instead of the empty string
'''


def get_string_made_first_and_last_2_chars(st):
    if len(st) < 2:
        return 'Empty String'
    res = st[:2] + st[-2:]
    return res


# print(get_string_made_first_and_last_2_chars('w3resource'))
# output:
# w3ce

'''
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
Sample String : 'restart'
Expected Result : 'resta$t'
'''


def change_occurence_of_the_first_char_1(st):
    l = list(st)
    for index, ch in enumerate(l):
        if ch == st[0] and index != 0:
             l[index]= '$'
    return ''.join(l)


def change_occurence_of_the_first_char_2(st):
    char0 = st[0]
    st = st.replace(char0, '$')
    res = char0 + st[1:]
    return res


# print(change_occurence_of_the_first_char_2('restart'))
# output:

'''
Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''


def swap_first_two_chars(st1, st2):
    first_two_chars_st1 = st1[:2]
    first_two_chars_st2 = st2[:2]
    res = first_two_chars_st2 + st1[2:] + ' ' + first_two_chars_st1 + st2[2:]
    return res


# print(swap_first_two_chars('abc', 'xyz'))
# output:
# xyc abz

'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged. Go to the editor
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''


def add_ing(st):
    if len(st) < 3:
        return st
    if st[-3:] == 'ing':
        return st + 'ly'
    return st + 'ing'


# print(add_ing('string'))
# output:
# stringly


'''
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''


def change_not_poor_into_good(st):
    index_not = st.find('not')
    index_poor = st.find('poor')
    if index_not < index_poor and index_not > 0 and index_poor > 0:
        st = st.replace(st[index_not:(index_poor+4)], 'good')
        return st
    else:
        return st


# print(change_not_poor_into_good('this is not that poor, this is poor'))
# output:
# this is good, this is poor


'''
Write a Python function that takes a list of words and returns the length of the longest one
'''


def longest_words(lis):
    lens_words = [len(word) for word in lis]
    longest_length = 0
    for word, length in zip(lis, lens_words):
        if length > longest_length:
            longest_length = length
    return longest_length


# print(longest_words(['df', 'dfdg', 'tryhdss', 'gdg', 'tjhtjas']))
# output:
# 7
'''
 Write a Python program to remove the nth index character from a nonempty string
'''


def remove_nth_char(n, st):
    return st[:n] + st[n+1:]


# print(remove_nth_char(3, 'dongdsgdf'))
# output:
# dondsgdf


'''
Write a Python program to change a given string to a new string where the first and last chars have been exchanged
'''


def exchange_firest_last_char(st):
    return st[-1] + st[1:-1] + st[0]


# print(exchange_firest_last_char('dongdgdf'))
# output:
# fongdgdd

'''
Write a Python program to remove the characters which have odd index values of a given string
'''


def remove_odd_index(st):
    s = ''
    for index in range(len(st)):
        if index % 2 == 0:
            s += st[index]
    return s


# print(remove_odd_index('dongxiang'))
# output:
# dnxag

'''
Write a Python program to count the occurrences of each word in a given sentence
'''


def count_occurrence_word(sentence):
    l = sentence.split(' ')
    keys = dict()
    for word in l:
        if word not in keys:
            keys[word] = 1
        else:
            keys[word] += 1
    return keys


# print(count_occurrence_word('the quick brown fox jumps over the lazy dog.'))
# output:
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1}


'''
Write a Python script that takes input from the user and displays that input back in upper and lower cases
'''


def upper_or_lower_st():
    st = input()
    print(st.upper())
    print(st.lower())


# upper_or_lower_st()
# dongxiang si agG  输入
# DONGXIANG SI AGG
# dongxiang si agg

'''
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''


def sort_words(words):
    l = words.split(', ')
    sorted_words = sorted(l)
    sorted_words = list(set(sorted_words))
    return ', '.join(sorted_words)


# print(sort_words('red, white, black, red, green, black'))
# output:
# white, red, black, green

'''
Write a Python function to create the HTML string with tags around the word(s)
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''


def add_tags(tag, st):
    return '<{0}>{1}</{2}>'.format(tag, st, tag)


# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))
# <i>Python</i>
# <b>Python Tutorial</b>


'''
Write a Python function to insert a string in the middle of a string. 
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''


def insert_string_middle(st, word):
    return st[:2] + word + st[2:]


# print(insert_string_middle('[[]]', 'python'))
# output:
# [[python]]

'''
Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
'''


def get_copy_last_two_chars(st):
    if len(st) < 2:
        print('the string length must be at least 2!')
        return
    return 4*st[-2:]


# print(get_copy_last_two_chars('python'))
# print(get_copy_last_two_chars('Exercises'))
# output:
# onononon
# eseseses

'''
Write a Python function to get a string made of its first three characters of a specified string. 
If the length of the string is less than 3 then return the original string. 
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
'''


def get_first_three_chars(st):
    if len(st) <= 3:
        return st
    return st[:3]


# print(get_first_three_chars('python'))
# print(get_first_three_chars('ipy'))
# pyt
# ipy

'''
Write a Python program to get the last part of a string before a specified character. 
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
'''


def get_last_part_string(st):
    print(st.split('/'))
    print(st.rsplit('/'))
    print(st.split('/', 1))
    print(st.split('/', 2))
    print(st.split('/', 3))
    return st.rsplit('/', 1)[0], st.rsplit('-', 1)[0]


# print(get_last_part_string('https://www.w3resource.com/python-exercises/string'))
# output:
# ['https:', '', 'www.w3resource.com', 'python-exercises', 'string']
# ['https:', '', 'www.w3resource.com', 'python-exercises', 'string']
# ['https:', '/www.w3resource.com/python-exercises/string']
# ['https:', '', 'www.w3resource.com/python-exercises/string']
# ['https:', '', 'www.w3resource.com', 'python-exercises/string']
# ('https://www.w3resource.com/python-exercises', 'https://www.w3resource.com/python')


