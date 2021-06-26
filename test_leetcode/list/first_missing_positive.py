

# 41. 缺失的第一个正数
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
#
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
# 示例 1：
#
# 输入：nums = [1,2,0]
# 输出：3
# 示例 2：
#
# 输入：nums = [3,4,-1,1]
# 输出：2
# 示例 3：
#
# 输入：nums = [7,8,9,11,12]
# 输出：1


class Solution:
    # 超时
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(1, n + 2):
            if i not in nums:
                return i

    def first_missing_positive(self, nums):
        n = len(nums)
        seen = set()
        for num in nums:
            seen.add(num)
        for i in range(1, n+1):
            if i not in seen:
                return i
        return n + 1

    def first_missing_positive2(self, nums):
        n = len(nums)
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                swap(nums, i, nums[i] - 1)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1



if __name__ == "__main__":
    solution = Solution()
    print(solution.first_missing_positive([1,2]))
