

#

class Solution:
    def maxArea(self, height) -> int:
        n = len(height)
        dp = [0]*(n)
        dp[1] = min(height[0:2])
        for i in range(2, n):
            j, max_i = 0, 0
            while j < i:
                tmp_area = min(height[i], height[j])*(i-j)
                if tmp_area > max_i:
                    max_i = tmp_area
                j += 1
            dp[i] = max(dp[i-1], max_i)
        return dp[-1]

    def max_area(self, height):
        n = len(height)
        left, right, ans = 0, n - 1, 0
        while left < right:
            tmp = min(height[left], height[right])*(right - left)
            ans = max(ans, tmp)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.max_area([1,8,6,2,5,4,8,3,7]))
