

# 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。


class Solution:
    # 超时
    def minSubArrayLen(self, target: int, nums) -> int:
        n = len(nums)
        min_len = n
        for i in range(n):
            sum_num, j = 0, i
            while j < n:
                sum_num += nums[j]
                if target <= sum_num:
                    min_len = min(min_len, j - i + 1)
                    break
                j += 1
        if sum(nums) < target:
            return 0
        return min_len

    # 滑动窗口
    def min_subarray_len(self, target, nums):
        n = len(nums)
        index = 0
        res, sum_num = float('inf'), 0
        for i in range(n):
            sum_num += nums[i]
            while sum_num >= target:
                res = min(res, i - index + 1)
                sum_num -= nums[index]
                index += 1
        return 0 if res == float('inf') else res


if __name__ == "__main__":
    solution = Solution()
    print(solution.min_subarray_len(7, [2,3,1,2,4,3]))
