

# 79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#


class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        path = []

        def back_track(i, j, depth, path):
            if depth == length:
                return True
            if 0 > i or i >= m or 0 > j or j >= n or (i, j) in path or \
                    board[i][j] != word[depth]:
                return False
            path.append((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if back_track(x, y, depth + 1, path):
                    return True
            path.pop()
            return False

        for i in range(m):
            for j in range(n):
                if back_track(i, j, 0, path):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
                         'ABCB'))
