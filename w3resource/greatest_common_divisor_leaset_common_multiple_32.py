

# lcm，取到两个数中的最大的数，然后循环加1，直到两个数都能整除
def get_greatest_common_divisor_and_least_common_multiple(num1, num2):
    result = 1
    cadidate = []
    for i in range(1, int(num1 / 2) + 1):
        for j in range(1, int(num2 / 2) + 1):
            if i == j and num1 % i == 0 and num2 % j == 0:
                cadidate.append(i)
                result *= i
    if len(cadidate) == 1 and cadidate[0] == 1:
        result = num2 * num1
    return cadidate[-1], result


# # gcd，随便取一个数，得到其中值，从大到小开始遍历，直到两个数都能整除
def get_greatest_common_divisor(num1, num2):
    gcd = 1
    if num1 % num2 == 0:
        return num2

    for x in range(int(num1 / 2), 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            gcd = x
            break
    return gcd


def get_leaset_common_multiple(num1, num2):
    if num1 > num2:
        z = num1
    else:
        z = num2
    while True:
        if (z % num1 == 0) and (z % num2 == 0):
            lcm = z
            break
        z += 1
    return lcm


if __name__ == '__main__':
    # print(get_greatest_common_divisor_and_least_common_multiple(48, 64))
    print(get_greatest_common_divisor(72, 64))
    print(get_leaset_common_multiple(24, 32))
