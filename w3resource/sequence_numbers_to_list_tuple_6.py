# Write a Python program which accepts a sequence of comma-separated numbers
# from user and generate a list and a tuple with those numbers.

# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


def numbers_to_list_tuple():
    data = str(input('please input a sequence of numbers:'))
    data = data.replace(' ', '')
    lis = data.split(',')
    print('List:', lis)
    tup = tuple(lis)
    print('Tuple:', tup)


if __name__ == '__main__':
    numbers_to_list_tuple()