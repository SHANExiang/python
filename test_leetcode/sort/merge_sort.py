

class Solution:
    def merge(self, nums, left, mid, right):
        p, q = left, mid + 1
        temp = [0] * len(nums)
        for i in range(left, right+1):
            temp[i] = nums[i]
        for j in range(left, right+1):
            if p > mid:
                nums[j] = temp[q]
                q += 1
            elif q > right:
                nums[j] = temp[p]
                p += 1
            elif temp[p] < temp[q]:
                nums[j] = temp[p]
                p += 1
            else:
                nums[j] = temp[q]
                q += 1

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) >> 1
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid+1, right)
        self.merge(nums, left, mid, right)

    def main(self, nums):
        left, right = 0, len(nums) - 1
        self.merge_sort(nums, left, right)
        return nums
