

# 33. 搜索旋转排序数组
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# [4,5,6,7,0,1,2]  7
# [4,5,6,0,1,2,4]
class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        index = 0
        for i in range(n):
            if i + 1 < n and nums[i] > nums[i+1]:
                index = i
                break
        def binary_search(nums, left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        x = binary_search(nums, 0, index)
        y = binary_search(nums, index+1, n - 1)
        if x != -1:
            return x
        if y != -1:
            return y
        return -1

    def search2(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4,], 4))
