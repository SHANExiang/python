

# 颠倒给定的 32 位无符号整数的二进制位。
#
# 示例 1：
#
# 输入: 00000010100101000001111010011100
# 输出: 00111001011110000010100101000000
# 解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
#      因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。


class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseBits(43261596))
