

# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#


class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def robot_range(nums, start, end):
            first = nums[start]
            second = max(nums[start], nums[start+1])
            for i in range(start+2, end):
                first, second = second, max(second, first + nums[i])
            return second
        return max(robot_range(nums, 0, n - 2), robot_range(nums, 1, n - 1))

