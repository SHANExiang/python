

class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ['']*n
        dp[0] = '1'
        if n >= 2:
            dp[1] = '11'
            for i in range(2, n):
                x, y, length = 0, 1, len(dp[i-1])
                tmp = ''
                while y < length:
                    if dp[i-1][x] == dp[i-1][y]:
                        y += 1
                        if y == length:
                            tmp += '%s%s' % (y - x, dp[i - 1][x])
                    else:
                        tmp += '%s%s' % (y - x, dp[i-1][x])
                        x = y
                        y = x + 1
                        if y == length:
                            tmp += '%s%s' % (y - x, dp[i - 1][x])
                dp[i] = tmp
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(3))



