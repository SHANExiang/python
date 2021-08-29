

# 给你一个整数数组nums ，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 如果存在这样的三元组下标 (i, j, k)且满足 i < j < k ，使得nums[i] < nums[j] < nums[k] ，返回 true ；否则，返回 false 。

# 示例 1：
#
# 输入：nums = [1,2,3,4,5]
# 输出：true
# 解释：任何 i < j < k 的三元组都满足题意
# 示例 2：
#
# 输入：nums = [5,4,3,2,1]
# 输出：false
# 解释：不存在满足题意的三元组
#


class Solution:
    # 超时
    def increasingTriplet(self, nums) -> bool:
        n = len(nums)
        for i in range(1, n-1):
            j, k = 0, i + 1
            flag = False
            while j < i:
                if nums[j] < nums[i]:
                    flag = True
                    break
                j += 1
            if not flag:
                continue
            while k < n:
                if nums[k] > nums[i]:
                    flag = True
                    break
                flag = False
                k += 1
            if flag:
                return True
        return False

    def increasingTriplet2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, mid = float('inf'), float('inf')
        for x in nums:
            if x <= small:
                small = x
            elif x <= mid:
                mid = x
            elif x > mid:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet2([2,1,5,0,4,6]))
    print(solution.increasingTriplet([1,2,3,4,5]))
