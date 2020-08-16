

def sorted_demo():
    lis01 = [2, 3, 56, 67, 1, 90]
    lis02 = sorted(lis01)
    print(id(lis01))
    print(id(lis02))

# 29
class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms
# 以上是java的那一套，但是就地操作显得很麻烦，比如
# oldResistor = OldResistor(23)
# oldResistor.set_ohms(oldResistor.get_ohms() + 23)
# python基本上不需要手动实现setter和getter方法，python中只需要
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
# 操作就是
# resistor = Resistor(23)
# resistor.ohms += 23   # 就地递增可以很方便


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms

# 然后VoltageResistance实例可以直接设置voltage的值，并且还把电流的值也计算出来

# ============================================================================
# 30. 闭包中使用外围作用域的变量


# 自定义比较器，根据列中的元素的索引为2的元素大小进行排序
# students_tuples = [('join','a',15),('kane','b',20),('pole','c',30)]
# students_tuples.sort(key=lambda student:student[2])
# print(students_tuples)
# output ---> [('join', 'a', 15), ('kane', 'b', 20), ('pole', 'c', 30)]


def sort_priority(values, group):
    def comparator(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=comparator)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 7, 5}
# sort_priority(numbers, group)
# print(numbers)
# output ---> [2, 3, 5, 7, 1, 4, 6, 8]

# lis =  [(1, 8), (0, 3), (1, 1), (0, 2), (0, 5), (1, 4), (0, 7), (1, 6)]
# lis.sort()
# print(lis)
# output ---> [(0, 2), (0, 3), (0, 5), (0, 7), (1, 1), (1, 4), (1, 6), (1, 8)]


def sort_priority1(values, group):
    found = False

    def comparator(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=comparator)
    return found


# found = sort_priority1(numbers, group)
# print('found==%s' % found)
# print(numbers)


def sort_priority2(values, group):
    found = False
    print(id(found)) # 140720592160624

    def comparator(x):
        nonlocal found
        if x in group:
            found = True
            print(id(found))  # 140720592160592
            return (0, x)
        return (1, x)
    values.sort(key=comparator)
    return found


# found = sort_priority2(numbers, group)
# print('found==%s' % found)
# print(numbers)

nonl = ['gfd', 'g', 546]


# def test_nonlocal():
#     nonlocal nonl
#     nonl = 4354
#     print(nonl)
# 会报错，说明nonlocal不能延伸到模块级别，这是为了防止它污染全局作用域。
#     nonlocal nonl
#     ^
# SyntaxError: no binding for nonlocal 'nonl' found

def test_global():
    # global nonl
    nonl = 'dgfghfh'
    print('id(nonl)==%s, nonl==%s' % (id(nonl), nonl))


print(id(nonl))
test_global()


def sort_priority3(values, group):
    found = [False]
    print(id(found)) # 140720592160624

    def comparator(x):
        if x in group:
            found[0] = True
            print(id(found))  # 140720592160592
            return (0, x)
        return (1, x)
    values.sort(key=comparator)
    return found[0]


found = sort_priority3(numbers, group)
print('found==%s' % found)
print(numbers)


if __name__ == '__main__':
    pass

