# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmp_value_list = list()
            tmp = []
            for node in queue:
                tmp_value_list.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(tmp_value_list)
            queue = tmp
        return res



