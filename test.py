

class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

    def remove_element(self, nums, val):
        left, n = 0, len(nums)
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left



if __name__ == "__main__":
    solution = Solution()
    print(solution.remove_element([-2, 3, 2, 1, -5], 2))
