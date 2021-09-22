
# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
#
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 示例2：
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
#    或者返回索引 5， 其峰值元素为 6。
#


class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums)
        left, right, ans = 0, n - 1, 0
        def get(i):
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        while left <= right:
            mid = (left + right)//2
            if get(mid-1) < get(mid) > get(mid+1):
                ans = mid
                break
            elif get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == "__main__":
    solutio = Solution()
    print(solutio.findPeakElement([1]))
