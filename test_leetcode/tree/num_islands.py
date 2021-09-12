

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3


class Solution:

    # 深度优先搜索
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j, grid):
            grid[i][j] = '0'
            for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y, grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j, grid)
        return res

    # 广度优先搜索
    def num_islands(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    import collections
                    neighbors = collections.deque([(i, j)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                neighbors.append((x, y))
                                grid[x][y] = '0'
        return res
