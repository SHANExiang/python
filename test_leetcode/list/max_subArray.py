

class Solution:
    '''
    给定一个整数数组
    nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


    '''
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)



