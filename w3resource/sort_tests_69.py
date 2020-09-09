

# Write a Python program to sort three integers without using conditional statements and loops.
def sort_integers():
    a = int(input('please input firset number:'))
    b = int(input('please input second number:'))
    c = int(input('please input third number:'))
    x = min(a, b, c)
    z = max(a, b, c)
    y = (a + b + c) - x - z
    print('numbers in sorted order,', x, y, z)


sort_integers()