import random
import timeit

'''
Write a Python program to create all possible strings by using 
'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
'''


def test_create_string_using_char():
    lis = ['a', 'e', 'i', 'o', 'u']
    s = set()
    start = timeit.default_timer()
    for x in range(1000):
        random.shuffle(lis)
        s.add(''.join(lis))
    end_time = timeit.default_timer() - start
    print('遍历1000次，耗时==', end_time, sep='')
    print('遍历1000次, 最终set长度==', len(s), sep='')

# test_create_string_using_char()
# 遍历1000次，耗时==0.0019216999999999984
# 遍历1000次, 最终set长度==120



