

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。


class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous = nums[len(nums) - 1]
            for j in range(len(nums)):
                tmp = nums[j]
                nums[j] = previous
                previous = tmp
        return nums

    # 三次反转
    def rotate2(self, nums, k):
        def swap(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        k = k % len(nums)
        swap(0, len(nums) - k -1)
        swap(len(nums) - k, len(nums) - 1)
        swap(0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    solution = Solution()
    # print(solution.rotate1([1, 2, 3, 4, 5, 6, 7], 3))
    print(solution.rotate2([1, 2, 3, 4, 5, 6, 7], 3))

