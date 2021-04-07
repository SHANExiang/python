

# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                return True and self.isSameTree(p.left, q.left) and self.isSameTree(
                    p.right, q.right)
            else:
                return False
        else:
            return False

    # 广度优先搜索
    def is_same_tree2(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        import collections
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])
        while queue2 and queue1:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1 = node1.left
            right1 = node1.right
            left2 = node2.left
            right2 = node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)
        return not queue1 and not queue2
