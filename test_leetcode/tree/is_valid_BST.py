
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            value = node.val
            if value >= upper or value <= lower:
                return False
            if not helper(node.right, value, upper):
                return False
            if not helper(node.left, lower, value):
                return False
            return True
        return helper(root)

    # 递归
    def is_valid_BST(self, root):
        if not root:
            return True

        def DFS(root, left, right):
            if not root:
                return True
            return left < root.val < right and DFS(root.left, left, root.val) and DFS(
                root.right, root.val, right)

        return DFS(root, float('-inf'), float('inf'))

    # 中序遍历
    def is_valid_BST2(self, root):
        stack, inorder = list(), float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
