

# 统计一个数字在排序数组中出现的次数。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
# 示例2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0


class Solution:
    def search(self, nums, target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j)//2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid - 1
        if j >= 0 and nums[j] != target:
            return 0
        right = i
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j)//2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid + 1
        left = j
        return right - left - 1

    def search2(self, nums, target):
        res = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                i, j = mid, mid + 1
                while 0 <= i:
                    if target == nums[i]:
                        i -= 1
                        res += 1
                    else:
                        break
                while j < len(nums):
                    if target == nums[j]:
                        j += 1
                        res += 1
                    else:
                        break
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([5,7,7,8,8,10], 8))
