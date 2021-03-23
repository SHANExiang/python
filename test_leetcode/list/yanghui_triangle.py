

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。


class Solution:
    def generate(self, numRows: int):
        res = list()
        for i in range(1, numRows+1):
            lis = list()
            if i == 1:
                lis = [1]
                res.append(lis)
            if i == 2:
                lis.append(1)
                lis.append(1)
                res.append(lis)
            if i > 2:
                lis.append(1)
                for j in range(1, i-1):
                    l = res[i-2][j-1] + res[i-2][j]
                    lis.append(l)
                lis.append(1)
                res.append(lis)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(7))



