

"""
有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""


class Solution:
    def is_valid_sudoku(self, board):
        def is_exist_duplicates(lis):
            for i in range(len(lis)):
                j = i + 1
                while j < len(lis):
                    if lis[i] == lis[j] and lis[i] != '.' and lis[j] != '.':
                        return True
                    else:
                        j += 1
            return False

        square_list = list()
        square_list.append(board[0][0:3] + board[1][0:3] + board[2][0:3])
        square_list.append(board[0][3:6] + board[1][3:6] + board[2][3:6])
        square_list.append(board[0][6:9] + board[1][6:9] + board[2][6:9])
        square_list.append(board[3][0:3] + board[4][0:3] + board[5][0:3])
        square_list.append(board[3][3:6] + board[4][3:6] + board[5][3:6])
        square_list.append(board[3][6:9] + board[4][6:9]+ board[5][6:9])
        square_list.append(board[6][0:3] + board[7][0:3] + board[8][0:3])
        square_list.append(board[6][3:6] + board[7][3:6] + board[8][3:6])
        square_list.append(board[6][6:9] + board[7][6:9] + board[8][6:9])

        for x in range(9):
            if is_exist_duplicates(square_list[x]):
                return False

        for x in range(9):
            if is_exist_duplicates(board[x]):
                return False

        vertical_list = list()
        for m in range(9):
            n = 0
            vertical_sub = list()
            while n < 9:
                vertical_sub.append(board[n][m])
                n += 1
            vertical_list.append(vertical_sub)
            if is_exist_duplicates(vertical_list[m]):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_valid_sudoku(
        [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]))

