import datetime
import re


def calculate_numbers_between_two_dates(date_tuple1, date_tuple2):
    date1 = datetime.datetime(year=date_tuple1[0], month=date_tuple1[1],
                              day=date_tuple1[2])
    date2 = datetime.datetime(year=date_tuple2[0], month=date_tuple2[1],
                              day=date_tuple2[2])
    if date_tuple1 >= date_tuple2:
        result = date1 - date2
        result = re.findall('(.*?)\sdays.*?', str(result))[0] + ' days'
    else:
        result = date2 - date1
        result = re.findall('(.*?)\sdays.*?', str(result))[0] + ' days'
    return result


if __name__ == '__main__':
    print(calculate_numbers_between_two_dates((2015, 4, 12), (2014, 5, 25)))
