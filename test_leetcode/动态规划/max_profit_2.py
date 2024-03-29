

# 给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 示例 1:
#
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[n-1][0]

    def max_profit2(self, prices):
        n = len(prices)
        i, res = 1, 0
        while i < n:
            res += max(0, prices[i] - prices[i-1])
            i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit(prices=[7,1,5,3,6,4]))
    print(solution.max_profit2(prices=[7,1,5,3,6,4]))
