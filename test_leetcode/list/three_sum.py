

# 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3 or not nums:
            return []
        nums.sort(reverse=False)
        res = list()
        for i in range(0, len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                find = 0 - nums[i] - nums[j]
                if find in nums[j+1:len(nums)]:
                    result = [nums[i], find, nums[j]]
                    if result not in res:
                        res.append(result)
        return res

    def threeSum1(self, nums):
        if len(nums) < 3 or not nums:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

    def threeSum3(self, nums):
        n = len(nums)
        if n < 3:
            return list()
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            left, right = index + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == -num:
                    temp = [num, nums[left], nums[right]]
                    if temp not in res:
                        res.append(temp)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(sorted([-1,0,1,2,-1,-4]))
    print(solution.threeSum1([-1,0,1,2,-1,-4]))
