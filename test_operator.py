

# print(2 & 3)
# print(-1 ^ -2)


def test_add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a


# print(test_add_without_plus_operator(2, 5))
# print(test_add_without_plus_operator(5, -9))
# print(test_add_without_plus_operator(-8, -3))
# 7
# -4
# -11
