from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [-4, -1, -1, 0, 1, 2]
class Solution:
    def threeSum(self, nums):
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
    print(solution.threeSum([-1,0,1,2,-1,-4]))
