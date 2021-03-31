
# 给你一个数组 nums和一个值val，你需要 原地 移除所有数值等于val的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeElement(self, nums, val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

    def remove_element1(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if val != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i



if __name__ == "__main__":
    solution = Solution()
    print(solution.remove_element1([0,1,2,2,3,0,4,2], 2))
