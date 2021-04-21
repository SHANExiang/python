# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
# 例如输入：
#
#   4
#  /  \
#  2   7
# / \  / \
# 1  3 6  9
# 镜像输出：
#
#    4
#  /  \
#  7  2
# / \ / \
# 9 6 3 1


# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        node = TreeNode(root.val)
        node.left = self.mirrorTree(root.right)
        node.right = self.mirrorTree(root.left)
        return node

    def mirror_tree(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.right
        return root


def print_node(root):
    if not root:
        return
    print(root.val, end=" ")
    print_node(root.left)
    print_node(root.right)


if __name__ == "__main__":
    # [4,2,7,1,3,6,9]
    root = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(6)
    node6 = TreeNode(9)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    solution = Solution()
    result = solution.mirrorTree(root)
    print_node(root)
    print(end="\n")
    print_node(result)
