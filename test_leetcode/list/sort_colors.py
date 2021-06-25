

#

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            if nums[left] == 2:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                elif nums[left] == nums[right]:
                    right -= 1
            else:
                left += 1
        left = 0
        while left < right:
            if nums[left] == 1:
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                elif nums[left] <= nums[right]:
                    right -= 1
            else:
                left += 1

    def sort_color(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        def quick_sort(nums, left, right):
            if left > right:
                return
            i, j = left, right
            pivot = nums[i]
            while i < j:
                while i < j and pivot <= nums[j]:
                    j -= 1
                nums[i] = nums[j]
                while i < j and pivot >= nums[i]:
                    i += 1
                nums[j] = nums[i]
            nums[j] = pivot
            quick_sort(nums, left, j-1)
            quick_sort(nums, j+1, right)
        quick_sort(nums, left, right)

    def sort_color2(self, nums):
        n = len(nums)
        p0, p1 = 0, 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1







if __name__ == "__main__":
    solution = Solution()
    solution.sort_color([0, 1, 0, 2])
