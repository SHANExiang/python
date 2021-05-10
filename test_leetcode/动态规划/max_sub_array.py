

# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释:连续子数组[4,-1,2,1]的和最大，为6。
#


class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        res_max = nums[0]
        dp = [0]*(n+1)
        dp[0] = res_max
        for i in range(1, n):
            if dp[i-1] >=0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            if dp[i] >  res_max:
                res_max = dp[i]
        return res_max


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
