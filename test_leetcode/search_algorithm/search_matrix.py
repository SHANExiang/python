

# 编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        index_h, index_v = 0, n - 1
        while index_h < m and index_v >= 0:
            if matrix[index_h][index_v] == target:
                return True
            elif target > matrix[index_h][index_v]:
                index_h += 1
            else:
                index_v -= 1
        return False
