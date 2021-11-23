# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
#
# 例如:
# 给定二叉树:[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归法
    def level_order1(self, root: TreeNode):
        res = []
        def helper(root, depth):
            if not root:
                return []
            if len(res) == depth: res.append([])
            res[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return res

    # 迭代法
    def level_order2(self, root):
        if not root:
            return []
        import collections
        queue, res = collections.deque(), []
        queue.append(root)
        res.append([root.val])
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res



