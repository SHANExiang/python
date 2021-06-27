

"""
给定一个 n×n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
"""
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# (3, 0)-->(0, 0)-->(0, 3)-->(3, 3)-->(3, 0)
# (2, 0)-->(0, 1)-->(1, 3)-->(3, 2)-->(2, 0)
# (1, 0)-->(0, 2)-->(2, 3)-->(3, 1)-->(1, 0)
# (1, 1)-->(1, 2)-->(2, 2)-->(2, 1)-->(1, 1)


class Solution:
    def rotate_matrix(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in range(n):
            for y in range(n):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for i in range(n):
            matrix[i].reverse()

    def rotate2(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n//2):
            for i in range(n-1-2*j):
                tmp1 = matrix[i+j][n-1-j]
                matrix[i+j][n-1-j] = matrix[j][i+j]
                tmp2 = matrix[n-1-j][n-1-i-j]
                matrix[n-1-j][n-1-i-j] = tmp1
                matrix[j][i+j] = matrix[n-1-i-j][j]
                matrix[n-1-i-j][j] = tmp2
        return matrix
