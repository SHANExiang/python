

class Solution(object):
    def remove_duplicates1(self, nums) -> int:
        n = 0
        while n < len(nums) - 1:
            if nums[n] == nums[n+1]:
                nums.remove(nums[n+1])
            else:
                n += 1
        return len(nums)

    def remove_duplicates2(self, nums):
        if not nums:
            return 0
        x = 0
        y = 1
        while y < len(nums):
            if nums[x] == nums[y]:
                nums.pop(y)
            else:
                x += 1
                y += 1
        return len(nums), nums


if __name__ == '__main__':
    solution = Solution()
    # print(solution.remove_duplicates1([0,0,1,1,1,2,2,3,3,4],))
    print(solution.remove_duplicates2([0,0,1,1,1,2,2,3,3,4],))
