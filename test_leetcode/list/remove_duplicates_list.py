

# 删除排序数组中的重复项
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


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

    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return n
        fast, slow = 1, 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == '__main__':
    solution = Solution()
    # print(solution.remove_duplicates1([0,0,1,1,1,2,2,3,3,4],))
    print(solution.remove_duplicates2([0,0,1,1,1,2,2,3,3,4],))
