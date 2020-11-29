

"""
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""


class Solution:
    def reverse(self, x: int) -> int:
        def reverse_list(s):
            left = 0
            right = len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        if x < 0:
            s = list(str(x)[1:])
            reverse_list(s)
            result = -int(''.join(s))
            return result if not result < -pow(2, 31) else 0
        else:
            s = list(str(x))
            reverse_list(s)
            result = int(''.join(s))
            return result if not result > pow(2, 31) - 1 else 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))
