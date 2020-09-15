

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


print('\"sdogong\"')
