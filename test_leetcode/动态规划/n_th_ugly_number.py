import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        temp = list()
        heapq.heappush(temp, 1)
        for i in range(1, n+1):
            ele = heapq.heappop(temp)
            if 2 * ele not in temp:
                heapq.heappush(temp, 2*ele)
            if 3 * ele not in temp:
                heapq.heappush(temp, 3*ele)
            if 5 * ele not in temp:
                heapq.heappush(temp, 5*ele)
        return ele

    def nth_ugly_number(self, n):
        dp, a, b, c = [1]*n, 0, 0, 0
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


if __name__ == "__main__":
    solution = Solution()
    print(solution.nth_ugly_number(12))
