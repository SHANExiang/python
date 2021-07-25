class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        tmp = list()
        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
        res = list()
        for i in range(r):
            res.append(tmp[c*i:c*i+c])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixReshape([[1,2],[3,4]], 4, 1))
