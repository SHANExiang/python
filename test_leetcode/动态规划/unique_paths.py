

# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#

# 示例 2：
#
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1
        destination = [(0, -1), (-1, 0)]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if n > 1:
            dp[0][1] = 1
        if m > 1:
            dp[1][0] = 1
        for i in range(m):
            for j in range(n):
                for x, y in destination:
                    i_pre, j_pre = i + x, j + y
                    if 0 <= i_pre < m and 0 <= j_pre < n:
                        dp[i][j] += dp[i_pre][j_pre]
        return dp[-1][-1]
