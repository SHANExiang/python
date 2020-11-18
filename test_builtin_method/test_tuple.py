from operator import itemgetter


'''
Write a Python program to find unique triplets whose three elements gives the
sum of zero from an array of n integers.
在一个n个数字的数组中，找出唯一的一个和为0的三元组
'''


def test_find_triplets_sum_of_zero(lis):
    result = []
    lis.sort()
    for x in range(len(lis) - 2):
        if x > 0 and lis[x] == lis[x - 1]:
            continue
        l, r = x + 1, len(lis) - 1
        while l < r:
            s = lis[l] + lis[x] + lis[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                if l < r and lis[l] == lis[l + 1]:
                    break
                if l < r and lis[r] == lis[r - 1]:
                     break
                result.append((lis[x], lis[l], lis[r]))
                break
    return result


lis = [1, -6, 4, 3, -1, 2, 0, -2, -3]
# print(test_find_triplets_sum_of_zero(lis))
# [(-6, 2, 4), (-3, -1, 4), (-2, -1, 3), (-1, 0, 1)]
# ****************************************************************************
''''
Write a Python program to sort a tuple by its float element. 
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''


def sorted_tuple(original_list):
    return sorted(original_list, key=itemgetter(1), reverse=True)


# print(sorted_tuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]))
# [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
