

# 二叉树的中序遍历


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        def inner(node):
            if node.left:
                inner(node.left)
            res.append(node.val)
            if node.right:
                inner(node.right)
        inner(root)
        return res

    def inorder_traversal(self, root):
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
