

# 34. 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#


class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        n = len(nums)
        left, right = 0, n - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if index == -1:
            return [-1, -1]
        x, y = index, index
        for i in range(index, -1, -1):
            if nums[i] != target:
                x = i + 1
                break
            else:
                x = i
        for j in range(index, n):
            if nums[j] != target:
                y = j - 1
                break
            else:
                y = j
        return [x, y]


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,10], 6))



