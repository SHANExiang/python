# Write a Python program to accept a filename from the
# user and print the extension of that.

# Sample filename : abc.java
# Output : java


# use list reverse
def get_extension_of_a_file1(file_name):
    lis = list(file_name)
    lis_copy = lis.copy()
    lis_copy.reverse()
    # print(lis_copy)
    i = lis_copy.index('.')
    # print(i)
    extension_name = ''.join(lis[-i:])
    # print(extension_name)
    return extension_name


# use split,get the last element
def get_extension_of_a_file2(file_name):
    lis = file_name.split('.')
    print(lis)
    return lis[-1]


if __name__ == '__main__':
    print(get_extension_of_a_file1('dong.xiang.java'))
    print(get_extension_of_a_file2('dong.xiang.java'))

