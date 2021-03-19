

class Solution:
    '''
    给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
    你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
    '''
    # 暴力法
    def max_profit1(self, prices) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

    # 一次遍历
    def max_profit2(self, prices):
        inf = int(1e9)
        min_price = inf
        max_price = 0
        for price in prices:
            max_price = max(price - min_price, max_price)
            min_price = min(min_price, price)
        return max_price

    # 动态规划
    def max_profit3(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            print(dp[i])
        return dp[-1]



if __name__ == "__main__":
    solution = Solution()
    print(solution.max_profit3([7,1,5,3,6,4]))





