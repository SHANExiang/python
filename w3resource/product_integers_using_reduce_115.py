from functools import reduce


def test_product_integers_using_reduce(lis):
    product = reduce((lambda x, y : x * y), lis)
    return product


print(test_product_integers_using_reduce([2, 34, 10]))



