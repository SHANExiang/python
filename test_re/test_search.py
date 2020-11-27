import re


def search_string_zero_b(string):
    pattern = 'ab*?'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_zero_b('bbabbbcc'))
# print(search_string_zero_b('a'))
# print(search_string_zero_b('acc'))
# print(search_string_zero_b('bcc'))
# ('found a match', 'a')
# ('found a match', 'a')
# ('found a match', 'a')
# not matched


"""
Write a Python program that matches a string that has an a followed by one or more b's.
"""


def search_string_one_b(string):
    pattern = 'ab+?'
    result = re.search(pattern, string)
    if result:
        return "found a match", result.group()
    else:
        return 'not matched'


# print(search_string_one_b('abc'))
# print(search_string_one_b('abbb'))
# print(search_string_one_b('aabbbc'))
# ('found a match', 'ab')
# ('found a match', 'ab')
# ('found a match', 'ab')


"""
Write a Python program that matches a string that has an a followed by zero or one 'b'.
"""


def search_string_zero_b_or_one(string):
    pattern = 'ab?'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not match'


# print(search_string_zero_b_or_one('ab'))
# print(search_string_zero_b_or_one('a'))
# print(search_string_zero_b_or_one('aaaabbbbcccc'))
# ('found a match', 'ab')
# ('found a match', 'a')
# ('found a match', 'a')

"""
Write a Python program that matches a string that has an a followed by three 'b'.
"""


def search_string_three_b(string):
    pattern = 'ab{3}?'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_three_b('abbbbb'))
# print(search_string_three_b('abaaabbbbb'))
# print(search_string_three_b('abbbabbbb'))
# ('found a match', 'abbb')
# ('found a match', 'abbb')
# ('found a match', 'abbb')

"""
Write a Python program that matches a string that has an a followed by two to three 'b'.
"""


def search_string_two_three_b(string):
    pattern = 'ab{2,3}?'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_two_three_b('abbabbbbb'))
# print(search_string_two_three_b('abbbbbccc'))
# print(search_string_two_three_b('ababccc'))
# ('found a match', 'abb')
# ('found a match', 'abb')
# not matched

"""
Write a Python program to find sequences of lowercase letters joined with a underscore.   
"""


def search_string_underscope_lowercase(string):
    pattern = '^[a-z]+_[a-z]+$'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_underscope_lowercase('aab_cbbbc'))
# print(search_string_underscope_lowercase('aab_Abbbc'))
# print(search_string_underscope_lowercase('Aaab_abbbc'))
# ('found a match', 'aab_cbbbc')
# not matched
# not matched


"""
Write a Python program to find the sequences of one upper case letter followed by lower case letters
"""


def search_string_upppercae_lowercase(string):
    pattern = '^[A-Z][a-z]+'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_upppercae_lowercase("AZdgfhg"))
# print(search_string_upppercae_lowercase("Azdgfhg"))
# print(search_string_upppercae_lowercase("dgZdgfhg"))
# not matched
# ('found a match', 'Azdgfhg')
# not matched


"""
Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. 
"""


def search_string_end_b(string):
    pattern = 'a.*?b$'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_end_b('fgadgth9b'))
# print(search_string_end_b('fgab'))
# print(search_string_end_b('fgabdgth9'))
# ('found a match', 'adgth9b')
# ('found a match', 'ab')
# not matched

"""
Write a Python program that matches a word at the beginning of a string.
"""


def match_word_at_beginning(string):
    pattern = '^\w+'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(match_word_at_beginning("The quick brown fox jumps over the lazy dog."))
# print(match_word_at_beginning(" The quick brown fox jumps over the lazy dog."))
# ('found a match', 'The')
# not matched

"""
Write a Python program that matches a word at the end of string, with optional punctuation
"""


def search_string_optional_punctuation(string):
    pattern = '\w+\S*$'
    result = re.search(pattern, string)
    if result:
        return 'found a match', result.group()
    else:
        return 'not matched'


# print(search_string_optional_punctuation("The quick brown fox jumps over the lazy dog."))
# print(search_string_optional_punctuation("The quick brown fox jumps over the lazy dog. "))
# ('found a match', 'dog.')
# not matched
