

"""
加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
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


if __name__ == "__main__":
    solution = Solution()
    print(solution.plus_one([6, 8, 8, 9]))
