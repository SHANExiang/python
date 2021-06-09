

# 279. 完全平方数
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#
#
# 示例 1：
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
# 提示：
#
# 1 <= n <= 104


class Solution(object):
    def num_square(self, n):
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]

        def min_num_square(k):
            if k in square_nums:
                return 1
            min_num = float("inf")
            for num in square_nums:
                if k < num:
                    break
                new_min_num_square = min_num_square(k-num) + 1
                min_num = min(min_num, new_min_num_square)
            return min_num
        return min_num_square(n)

    def num_square2(self, n):
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for k in square_nums:
                if i < k:
                    break
                dp[i] = min(dp[i], dp[i-k]+1)
        return dp[-1]




if __name__ == "__main__":
    solution = Solution()
    print(solution.num_square(13))