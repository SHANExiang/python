

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
# 示例：
#
# 输入：nums =[1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#


class Solution:
    def exchange(self, nums):
        def func(num):
            if num % 2 == 0:
                return 1
            else:
                return 0
        nums = sorted(nums, key=func)
        return nums

    def exchange2(self, nums):
        i, j = 0, len(nums) - 1
        while i != j and i < j:
            if nums[i] % 2 == 0:
                if nums[j] % 2 == 0:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            else:
                if nums[j] % 2 == 0:
                    i += 1
                    j -= 1
                else:
                    i += 1
        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.exchange2([1]))
