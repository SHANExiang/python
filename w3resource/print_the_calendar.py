import calendar
# Write a Python program to print the calendar of a given month and year.


def print_calendar(year, month):
    # Write a Python program to print the documents (syntax, description etc.)
    # of Python built-in function(s).
    print(abs.__doc__)
    return calendar.month(year, month)


if __name__ == '__main__':
    year = int(input('Input the year:'))
    month = int(input('Input the month:'))
    print(print_calendar(year, month))