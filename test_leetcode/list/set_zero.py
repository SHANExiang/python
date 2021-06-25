

# 73. 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
# 进阶：
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        seen = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    seen.append((i, j))
        for x in seen:
            for i in range(n):
                matrix[x[0]][i] = 0
            for j in range(m):
                matrix[j][x[1]] = 0
        print(matrix)


if __name__ == "__main__":
    solution = Solution()
    solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
