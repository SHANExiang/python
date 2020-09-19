

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


print(test_get_n_from_degrees_number2_written_sequentially_in_line_no_spaces('2481632'))
