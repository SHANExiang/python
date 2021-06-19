

# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
#
#
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
# 提示：
#
# 0 <= nums.length <= 104
# -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        max_len = 1
        i, j = 0, 1
        nums.sort()
        while i < j < n:
            if nums[j] == nums[j-1] + 1:
                j += 1
                if j == n:
                    max_len = max(max_len, j - i)
            elif nums[j] == nums[j-1]:
                i += 1
                j += 1
                if j == n:
                    max_len = max(max_len, j - i)
            else:
                max_len = max(max_len, j - i)
                i = j
                j = i + 1
        return max_len

    def longest_consecutive(self, nums):
        if not nums:
            return 0
        n, max_len = len(nums), 1
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_len = 1
                num += 1
                while num in nums_set:
                    current_len += 1
                    num += 1
                max_len = max(max_len, current_len)
        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_consecutive([100,4,200,1,3,2, 1, 2]))

