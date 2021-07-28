

class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        path = dict()

        def back_track(i, j, path, index):
            if i >= m or i < 0 or j >= n or j < 0 or index >= len(word) or word[index] != board[i][j]:
                return False
            if (i, j) in path:
                return False
            path[(i, j)] = board[i][j]
            if ''.join(path.values()) == word:
                return True
            if back_track(i+1, j, path, index+1) or back_track(i-1, j, path, index+1) or \
                    back_track(i, j + 1, path, index+1) or back_track(i, j - 1, path, index+1):
                return True
            path.pop((i, j))
            return False
        for i in range(m):
            for j in range(n):
                if back_track(i, j, path, 0):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
    print(solution.exist(board = [["a","b"],["c","d"]], word = "abdc"))
    print(solution.exist([["a","a"]], "aaa"))
