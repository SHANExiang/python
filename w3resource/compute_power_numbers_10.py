# Write a Python program that accepts an integer (n) and
# computes the value of n+nn+nnn.

# Sample value of n is 5
# Expected Result : 615


def compute_power_number1(number):
    # number + number*10 + number + number + number*10 + number*100
    return 3*number + 2*number*10 + number*100


def compute_power_number2(number):
    num1 = int("%s" % number)
    num2 = int("%s%s" % (number, number))
    num3 = int("%s%s%s" % (number, number, number))
    return num1 + num2 + num3


if __name__ == '__main__':
    number = int(input('please input a number:'))
    print(compute_power_number1(number))
    print(compute_power_number2(number))