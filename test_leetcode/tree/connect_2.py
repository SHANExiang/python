

# 给定一个二叉树

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有next 指针都被设置为 NULL。


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 层序遍历解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:  # 遍历每一层
            length = len(queue)
            tail = None # 每一层维护一个尾节点
            for i in range(length): # 遍历当前层
                curnode = queue.pop(0)
                if tail:
                    tail.next = curnode # 让尾节点指向当前节点
                tail = curnode # 让当前节点成为尾节点
                if curnode.left : queue.append(curnode.left)
                if curnode.right: queue.append(curnode.right)
        return root

    # # 链表解法
    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        while first:  # 遍历每一层
            dummyHead = Node(None)  # 为下一行创建一个虚拟头节点，相当于下一行所有节点链表的头结点(每一层都会创建)；
            tail = dummyHead  # 为下一行维护一个尾节点指针（初始化是虚拟节点）
            cur = first
            while cur:  # 遍历当前层的节点
                if cur.left:  # 链接下一行的节点
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next  # cur同层移动到下一节点
            first = dummyHead.next  # 此处为换行操作，更新到下一行
        return root
