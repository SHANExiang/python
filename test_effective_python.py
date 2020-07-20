

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
# 30






if __name__ == '__main__':
    sorted_demo()
