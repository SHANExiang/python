

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

    def reverse_int(self, x):
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))
