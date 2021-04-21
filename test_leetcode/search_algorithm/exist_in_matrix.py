

# 给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word存在于网格中，返回true ；否则，返回false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
#


class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        flag = [[False for i in range(n)] for j in range(m)]

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if flag[row][col] or board[row][col] != word[index]:
                return False
            flag[row][col] = True
            if dfs(row+1, col, index+1) or dfs(row-1, col, index+1) \
                    or dfs(row, col+1, index+1) or dfs(row, col-1, index+1):
                return True
            flag[row][col] = False
            return False
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(i, j, 0):
                    return True
        return False
