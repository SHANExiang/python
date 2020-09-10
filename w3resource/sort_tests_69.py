

# Write a Python program to sort three integers without using conditional statements and loops.
def sort_three_integers():
    a = int(input('please input firset number:'))
    b = int(input('please input second number:'))
    c = int(input('please input third number:'))
    x = min(a, b, c)
    z = max(a, b, c)
    y = (a + b + c) - x - z
    print('numbers in sorted order,', x, y, z)


# Write a Python program to sort files by date.
def sort_files_by_date():
    import glob
    import os
    import datetime
    files = glob.glob('*.py')
    files.sort(key=os.path.getmtime)
    for x in files:
        print('%s %s' % (x, datetime.datetime.fromtimestamp(os.path.getmtime(x))))


if __name__ == '__main__':
    # sort_three_integers()
    # numbers in sorted order, 23 45 100

    sort_files_by_date()

