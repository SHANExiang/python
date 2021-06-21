

# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#


class Solution:
    def exist(self, board, word: str) -> bool:
        length = len(word)
        m = len(board)
        n = len(board[0])
        def dfs(cur, i, j):
            if cur >= length:
                return False
            if i >= m or i < 0 or j >= n or j < 0:
                return False
            if cur == length - 1:
                return True
            if board[i][j] != word[cur]:
                return False
            tmp = board[i][j]
            board[i][j] = '.'
            res = dfs(cur+1, i+1, j) or dfs(cur+1, i-1, j) or dfs(cur+1, i, j+1) or dfs(cur+1, i, j-1)
            board[i][j] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False

