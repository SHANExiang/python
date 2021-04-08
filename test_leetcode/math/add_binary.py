

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                b = "0" + b
        elif len(a) < len(b):
            for i in range(len(b) - len(a)):
                a = "0" + a

        def add(x, y, mod):
            print('x-%s==y-%s' % (x, y))
            if not x and not y:
                if mod == "1":
                    return mod
                else:
                    return ""
            else:
                if x[-1] == y[-1] == "1":
                    if mod == "1":
                        return add(x[0:-1], y[0:-1], "1") + "1"
                    return add(x[0:-1], y[0:-1], "1") + "0"
                elif x[-1] == "1" and y[-1] == "0" or y[-1] == "1" and x[-1] == "0":
                    if mod == "1":
                        return add(x[0:-1], y[0:-1], "1") + "0"
                    return add(x[0:-1], y[0:-1], "0") + "1"
                else:
                    if mod == "1":
                        return add(x[0:-1], y[0:-1], "0") + "1"
                    return add(x[0:-1], y[0:-1], "0") + "0"
        return add(a, b, "0")


if __name__ == "__main__":
    solution = Solution()
    # print(solution.addBinary('11', '1'))
    # print(solution.addBinary('1010', '1011'))
    # print(solution.addBinary('0', '0'))
    print(int("11", 2))
    print("{0:b}".format(11))
    print("a ".strip().split(" "))

