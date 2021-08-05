

# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 示例 1:
#
# 输入: [0,1,3]
# 输出: 2
# 示例2:
#
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
#


class Solution:
    def missingNumber(self, nums) -> int:
        res = n = len(nums)
        for i in range(n):
            res ^= i ^ nums[i]
        return res

    def missing_number(self, nums):
        n = len(nums) - 1
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def missingNumber2(self, nums) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] != i:
                return i
            i += 1
        return n


if __name__ == "__main__":
    solution = Solution()
    print(solution.missing_number([0]))

