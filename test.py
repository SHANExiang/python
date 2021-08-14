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
    def sortedArrayToBST(self, nums) -> TreeNode:
        n = len(nums)
        left_index, right_index = 0, n - 1

        def recur(left, right):
            if left > right:
                return
            mid = (right + left)//2
            root = TreeNode(nums[mid])
            root.left = recur(left, mid-1)
            root.right = recur(mid+1, right)
            return root
        return recur(left_index, right_index)


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedArrayToBST([-10,-3,0,5,9]))
