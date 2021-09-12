
# 给定一棵二叉搜索树，请找出其中第k大的节点。

# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#   2
# 输出: 4
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root, k: int) -> int:
        res = list()

        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res[len(res) - k]

    def kthlargest(self, root, k):
        self.k = k

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        dfs(root)
        return self.res

    def kth_larget2(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.left

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]


if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(6)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    node6 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    # node2.left = node5
    node3.left = node6
    solution = Solution()
    print(solution.kthLargest(root, 2))
