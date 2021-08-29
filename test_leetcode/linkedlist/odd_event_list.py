

# 奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        cur = head
        if cur.next:
            odd_cur = head.next.next
            event_cur = head.next
            point = event_cur
            while odd_cur:
                cur.next = odd_cur
                point.next = odd_cur.next
                point = point.next
                if odd_cur.next:
                    odd_cur = odd_cur.next.next
                else:
                    odd_cur = None
                cur = cur.next
            cur.next = event_cur
        return head

    def oddEvenList2(self, head: ListNode) -> ListNode:
        pre = odd = ListNode(0)
        event = cur = ListNode(0)
        while head:
            odd.next = head
            odd = odd.next
            cur.next = head.next
            if cur.next:
                cur = cur.next
            head = head.next
            if head:
                head = head.next
            else:
                break
        odd.next = event.next
        return pre.next


if __name__ == "__main__":
    node7 = ListNode(7)
    node6 = ListNode(4, node7)
    node5 = ListNode(6, node6)
    node4 = ListNode(5, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(1, node3)
    head = ListNode(2, node2)

    #  2->1->3->5->6->4->7-null
    solution = Solution()
    head = solution.oddEvenList2(head)
    while head:
        print(head.val)
        head = head.next
