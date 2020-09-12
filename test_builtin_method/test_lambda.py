

# Write a Python program to get numbers divisible by fifteen from a list
# using an anonymous function
def test_division_5_in_list(lis):
    return list(filter(lambda x : x % 5 == 0, lis))


print(test_division_5_in_list([35, 25, 20, 71, 55]))
# [35, 25, 20, 55]
