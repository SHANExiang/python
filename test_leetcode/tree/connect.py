

# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有next 指针都被设置为 NULL。
#
# 进阶：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        root.next = None

        def recur(node):
            if not node:
                return
            cur = node
            while node:
                if node.left and node.right:
                    node.left.next = node.right
                if node.next and node.right:
                    node.right.next = node.next.left
                node = node.next

            recur(cur.left)
            recur(cur.right)

        recur(root)
        return root

    def connect2(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left and root.right:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect2(root.left)
        self.connect2(root.right)
        return root
