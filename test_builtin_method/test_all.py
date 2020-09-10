

# Write a Python program to test whether all numbers of a list is greater than a certain number.
def test_all():
    numbers = [23, 34, 12, 45]
    print(all(x > 20 for x in numbers))
    print(all(x < 100 for x in numbers))


# test_all()
# False
# True