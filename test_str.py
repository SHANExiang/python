

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

test_string_convert_integer_list()
# [65, 66, 109]
