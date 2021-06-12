

# 238. 除自身以外数组的乘积
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
#
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


class Solution:
    def productExceptSelf(self, nums):
        def helper(lis, i, j):
            index, res = i, 1
            while index < j:
                res *= lis[index]
                index += 1
            return res
        n = len(nums)
        ret = [0]*n
        for i, ele in enumerate(nums):
            ret[i] = helper(nums, i+1, n)*helper(nums, 0, i)
        return ret

    def product_except_self(self, nums):
        n = len(nums)
        L, R, res = [0]*n, [0]*n, [0]*n
        L[0] = 1
        for i in range(1, n):
            L[i] = L[i-1]*nums[i-1]
        R[n-1] = 1
        for j in range(n-2, -1, -1):
            R[j] = R[j+1]*nums[j+1]
        for k in range(n):
            res[k] = L[k]*R[k]
        return res

    def product_except_self2(self, nums):
        n = len(nums)
        L = [0]*n
        L[0] = 1
        for i in range(1, n):
            L[i] = L[i-1]*nums[i-1]
        R = 1
        for j in range(n-1, -1, -1):
            L[j] = L[j]*R
            R *= nums[j]
        return L


if __name__ == "__main__":
    solution = Solution()
    print(solution.product_except_self2([1, 2, 3, 4]))
