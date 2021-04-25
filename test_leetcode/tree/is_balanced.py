
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root) -> bool:
        if not root:
            return True
        def get_depth(root):
            if not root:
                return 0
            return 1 + max(get_depth(root.left), get_depth(root.right))
        if -1 <= get_depth(root.left) - get_depth(root.right) <= 1 and \
                self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
