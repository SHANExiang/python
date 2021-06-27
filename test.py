

# 1 2 3 (0,0),(0,1),(0,3)
# 4 5 6 (1,0),(1,1),(1,2)
# 7 8 9 (2,0),(2,1),(2,2)


class Solution:
    def rotate(self, matrix):
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


if __name__ == "__main__":
    solution = Solution()
    matrix = solution.rotate([[1]])
    for x in range(len(matrix)):
        print(matrix[x])
