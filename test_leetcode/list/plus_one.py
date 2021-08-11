

"""
加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution:
    def plus_one(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            if digits[0] == 9 and len(digits) == 1:
                return [1, 0]
            else:
                digits[-1] = 0
                return self.plus_one(digits[:-1]) + [digits[-1]]

    def plusOne(self, digits):
        n, plus = len(digits), 1
        right = n - 1
        while right >= 0:
            s = digits[right] + plus
            if s >= 10:
                plus = 1
                digits[right] = 0
            else:
                plus = 0
                digits[right] = s
                break
            right -= 1
        if plus == 0:
            return digits
        res = [1]
        res.extend(digits)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.plus_one([6, 8, 8, 9]))
