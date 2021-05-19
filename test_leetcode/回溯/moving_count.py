

# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
# 但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
#


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        result = set()

        def helper(num):
            res = 0
            while num > 0:
                res += num%10
                num //= 10
            return res

        def back_track(i, j):
            sum_i = helper(i)
            sum_j = helper(j)
            if i < 0 or i >= m or j < 0 or j >= n or sum_j + sum_i > k or \
                    (i, j) in result:
                return
            result.add((i, j))
            back_track(i+1, j)
            back_track(i-1, j)
            back_track(i, j-1)
            back_track(i, j+1)
        back_track(0, 0)
        return len(result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.movingCount(2, 3, 4))



