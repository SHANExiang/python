import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        today_time = time.localtime()
        print(today_time)
        return cls(today_time.tm_year, today_time.tm_mon, today_time.tm_mday)

    @classmethod
    def today2(cls):
        d = cls.__new__(cls)
        today_time = time.localtime()
        d.year = today_time.tm_year
        d.month = today_time.tm_mon
        d.day = today_time.tm_mday
        return d


if __name__ == '__main__':
    d = Date(2020, 7, 19)
    print(d)
    print(Date.today())
