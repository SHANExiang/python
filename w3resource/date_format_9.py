# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).

# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014


def date_format1(date):
    return "{0} / {1} / {2}".format(date[0], date[1], date[2])


# use %s
def date_format2(date):
    return "%s / %s / %s" % date


if __name__ == '__main__':
    date = (11, 12, 2014)
    print(date_format1(date=date))
    print(date_format2(date=date))
