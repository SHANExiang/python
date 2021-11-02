

"""
两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
"""


class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if target == nums[i] + nums[j]:
                    return [i, j]
                else:
                    j += 1

    def two_sum2(self, nums, target):
        dic = dict()
        for index, num in enumerate(nums):
            if target - num not in dic:
                dic[num] = index
            else:
                return [index, dic[target - num]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum2([11, 7, 11, 2], 9))


