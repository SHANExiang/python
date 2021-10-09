

# 螺旋矩阵II
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#


class Solution:
    def generateMatrix(self, n: int):
        destination = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        temp = 2
        res[0][0] = 1
        used = [(0, 0)]
        for _ in range(n):
            for x, y in destination:
                i = x + i
                j = y + j
                while 0 <= i < n and 0 <= j < n and (i, j) not in used:
                    used.append((i, j))
                    res[i][j] = temp
                    i = x + i
                    j = y + j
                    temp += 1
                i -= x
                j -= y
        return res

    def generate_matrix(self, n):
        left, right, up, down = 0, n - 1, 0, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        while up < down and left < right:
            for i in range(left, right):
                res[up][i] = num
                num += 1

            for j in range(up, down):
                res[j][right] = num
                num += 1

            for i in range(right, left, -1):
                res[down][i] = num
                num += 1

            for j in range(down, up, -1):
                res[j][left] = num
                num += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        if n % 2:
            res[n//2][n//2] = num
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.generate_matrix(4))
