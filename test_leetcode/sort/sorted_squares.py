

# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 示例 1：
#
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]


class Solution:
    # 暴力法
    def sortedSquares(self, nums):
        nums = [num*num for num in nums]
        nums.sort()
        return nums

    def sorted_squares(self, nums):
        n = len(nums)
        left, right = 0, n - 1
        cur = n - 1
        res = [-1] * n
        while left <= right:
            if nums[left]*nums[left] < nums[right]*nums[right]:
                res[cur] = nums[right]*nums[right]
                right -= 1
            else:
                res[cur] = nums[left]*nums[left]
                left += 1
            cur -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.sorted_squares([-4,-1,0,0,3,10]))

