class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            if s[i - 2:i] > '25' or s[i - 2:i] < '10':
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 2] + dp[i - 1]
            print(dp[i])
        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.translateNum(18822))
