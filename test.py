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

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red, blue = 0, n - 1
        cur = 0
        while cur < n and blue > cur:
            if nums[cur] == 0:
                if nums[red] != 0:
                    nums[cur], nums[red] = nums[red], nums[cur]
                else:
                    cur += 1
                red += 1
            elif nums[cur] == 2:
                if nums[blue] != 2:
                    nums[cur], nums[blue] = nums[blue], nums[cur]
                else:
                    cur += 1
                blue -= 1
            else:
                cur += 1
        print(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortColors([2,0,1]))
