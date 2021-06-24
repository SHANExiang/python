

# 54. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return list()
        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for j in range(top+1, bottom+1):
                res.append(matrix[j][right])
            if left < right and top < bottom:
                for i in range(right-1, left, -1):
                    res.append(matrix[bottom][i])
                for j in range(bottom, top, -1):
                    res.append(matrix[j][left])
            left += 1
            right -= 1
            bottom -= 1
            top += 1
        return res

    def spiral_order(self, matrix):
        if not matrix or not matrix[0]:
            return list()
        m, n = len(matrix), len(matrix[0])
        visted = [[False]*n for _ in range(m)]
        destination = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_num = m * n
        res = [0] * total_num
        i, j = 0, 0
        index = 0
        for k in range(total_num):
            res[k] = matrix[i][j]
            visted[i][j] = True
            next_i, next_j = destination[index][0] + i, destination[index][1] + j
            if not (0 <= next_i < m and 0 <= next_j < n and not visted[next_i][next_j]):
                index = (1+index) % 4
            i, j = destination[index][0] + i, destination[index][1] + j
        return res



# 1 2 3 4
# 5 6 7 8
# 9 10 11 12


if __name__ == "__main__":
    solution = Solution()
    print(solution.spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
