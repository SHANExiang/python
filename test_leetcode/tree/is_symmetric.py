

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            tmp = []
            node_list = []
            for node in queue:
                if node.left:
                    tmp.append(node.left.val)
                    node_list.append(node.left)
                else:
                    tmp.append('null')
                if node.right:
                    tmp.append(node.right.val)
                    node_list.append(node.right)
                else:
                    tmp.append('null')
            if tmp == tmp[::-1]:
                queue = node_list
            else:
                return False
        return True

    def is_symmetric(self, root: TreeNode) -> bool:
        def is_sysmmetric_tree(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return is_sysmmetric_tree(left.left, left.right) & \
                   is_sysmmetric_tree(right.left, right.right)
        if not root:
            return True
        return is_sysmmetric_tree(root.left, root.right)
