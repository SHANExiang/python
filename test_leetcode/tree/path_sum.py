# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# 给定如下二叉树，以及目标和 target = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        res, path = [], []

        def recur(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, target)
            recur(root.right, target)
            path.pop()
        recur(root, target)
        return res


if __name__ == "__main__":
    root = TreeNode(5)
    Node1 = TreeNode(4)
    Node2 = TreeNode(8)
    Node3 = TreeNode(11)
    Node4 = TreeNode(13)
    Node5 = TreeNode(4)
    Node6 = TreeNode(7)
    Node7 = TreeNode(2)
    Node8 = TreeNode(5)
    Node9 = TreeNode(1)
    root.left = Node1
    root.right = Node2
    Node1.left = Node3
    Node2.left = Node4
    Node2.right = Node5
    Node3.left = Node6
    Node3.right = Node7
    Node4.left = Node8
    Node4.right = Node9
    solution = Solution()
    print(solution.pathSum(root, 22))
