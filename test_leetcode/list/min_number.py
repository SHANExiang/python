

# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 示例 1:
#
# 输入: [10,2]
# 输出: "102"
# 示例2:
#
# 输入: [3,30,34,5,9]
# 输出: "3033459"


class Solution:
    def minNumber(self, nums) -> str:
        def inner(a, b):
            x, y = a + b, b + a
            if x > y:
                return 1
            elif y < x:
                return -1
            else:
                return 0
        import functools
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(inner))
        return ''.join(strs)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minNumber([3,30,34,5,9]))





