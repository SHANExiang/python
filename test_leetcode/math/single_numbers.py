

# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#


class Solution:
    def singleNumbers(self, nums):
        nums.sort()
        res = list()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                res.append(nums[i])
            if len(res) == 2:
                break
            if nums[i] == nums[i+1]:
                i += 2
            else:
                res.append(nums[i])
                i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumbers([4, 1, 4, 6]))
