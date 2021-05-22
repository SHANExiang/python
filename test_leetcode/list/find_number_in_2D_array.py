

# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target=5，返回true。
#
# 给定target=20，返回false。
#


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        if target > matrix[n - 1][m - 1] or target < matrix[0][0]:
            return False
        h, v = (n - 1)//2, (m - 1)//2
        if target == matrix[h][v]:
            return True
        elif target < matrix[h][v]:
            return self.findNumberIn2DArray([l[0:v] for l in matrix[0:h+1]], target)
        else:
            return self.findNumberIn2DArray([l[v+1:m] for l in matrix[0:h]], target) or \
                   self.findNumberIn2DArray([l[v+1:m] for l in matrix[h+1:n]], target) or \
                   self.findNumberIn2DArray([l[0:v] for l in matrix[h+1:n]], target)

    def find_number_in_2D_array(self, matrix, target):
        i, j = len(matrix) - 1, 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False

if __name__ == "__main__":
    solution = Solution()
    s = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
    ]

    print(solution.findNumberIn2DArray(s, 20))


