

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root

    def sortedArrayToBST2(self, nums) -> TreeNode:
        n = len(nums)
        left_index, right_index = 0, n - 1

        def recur(left, right):
            if left > right:
                return
            mid = (right + left) // 2
            root = TreeNode(nums[mid])
            root.left = recur(left, mid - 1)
            root.right = recur(mid + 1, right)
            return root

        return recur(left_index, right_index)
