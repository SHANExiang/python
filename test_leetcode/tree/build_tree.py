

# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
# 例如，给出
#
# 前序遍历 preorder =[3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def recur(pre_root, in_left, in_right):
            if in_left > in_right:
                return
            node = TreeNode(preorder[pre_root])
            index = dic.get(preorder[pre_root])
            node.left = recur(pre_root + 1, in_left, index - 1)
            node.right = recur(pre_root + index - in_left + 1, index + 1, in_right)
            return node
        dic = dict()
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

    def build_tree(self, preorder, inorder):
        if not preorder:
            return
        node = TreeNode(preorder[0])
        left_length = inorder.index(preorder[0])
        left_preorder = preorder[1:left_length + 1]
        left_inorder = inorder[0:left_length]
        right_preorder = preorder[left_length + 1:]
        right_inorder = inorder[left_length + 1:]
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node
