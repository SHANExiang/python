

# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [0]*n, 0, 0, 0
        dp[0] = 1
        for i in range(1, n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

    def nth_ugly_number(self, n):
        import heapq
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]
        for i in range(1, n):
            cur = heapq.heappop(heap)
            for ele in [cur*num for num in factors]:
                if ele not in seen:
                    seen.add(ele)
                    heapq.heappush(heap, ele)
        return heapq.heappop(heap)


if __name__ == "__main__":
    solution = Solution()
    # solution.nthUglyNumber(4)
    solution.nth_ugly_number(4)
