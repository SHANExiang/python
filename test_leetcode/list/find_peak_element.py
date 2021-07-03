


class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if i == 0:
                if i + 1 < n:
                    if nums[i] > nums[i+1]:
                        return i
                else:
                    return 0
            if i == n - 1:
                if nums[i] > nums[i-1]:
                    return i
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i += 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1,2,1,3,5,6,4]))