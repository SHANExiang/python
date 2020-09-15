import collections


def test_sum_numbers_counts():
    num = [2, 3, 4, 3, 3, 0, 10, 4, 4, 4]
    c = collections.Counter(num)
    print(c, c.items(), type(c.items()))
    print(sum(c.values())) # 求数字出现次数的和


test_sum_numbers_counts()
# Counter({4: 4, 3: 3, 2: 1, 0: 1, 10: 1}) dict_items([(2, 1), (3, 3), (4, 4), (0, 1), (10, 1)]) <class 'dict_items'>
# 10

