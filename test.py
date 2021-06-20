

class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, 1
        while i <= j < n:
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([0,1,2]))
