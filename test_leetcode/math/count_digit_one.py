

# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
# 示例 1：
#
# 输入：n = 12
# 输出：5
# 示例 2：
#
# 输入：n = 13
# 输出：6


class Solution:
    def count(self, num):
        time = 0
        while num >= 1:
            if num % 10 == 1:
                time += 1
            num = num // 10
        return time

    def countDigitOne(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + self.count(i)
        return dp[-1]

    def count_digit_one2(self, n):
        res = 0
        for i in range(n + 1):
            res += self.count(i)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.countDigitOne(12))
