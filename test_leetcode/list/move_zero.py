

"""
移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def move_zeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(x, y):
            tmp = nums[x]
            nums[x] = nums[y]
            nums[y] = tmp
        left = 0
        length = len(nums) - 1
        right = 1
        while left <= length - 1 and right <= length:
            if nums[left] == 0:
                if nums[right] == 0:
                    right += 1
                else:
                    swap(left, right)
                    left += 1
            else:
                left += 1
                right += 1


if __name__ == "__main__":
    nums = [0, 0, 0, 1, 0]
    solution = Solution()
    solution.move_zeroes(nums)
    print(nums)
