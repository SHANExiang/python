

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if [] == [] or lists == [[]]:
            return None
        min_node_value = min(lists, key=lambda x: x.val)
        for node in lists:
            if node.val == min_node_value.val:
                lists.remove(node)
                if node.next:
                    lists.append(node.next)
                node.next = self.mergeKLists(lists)
                return node

    def merge_k_lists(self, lists):
        def merge_two_lists2(l1, l2):
            head = ListNode(-1)
            prev = head
            while l1 and l2:
                if l1.val >= l2.val:
                    prev.next = l2
                    l2 = l2.next
                else:
                    prev.next = l1
                    l1 = l1.next
                prev = prev.next
            prev.next = l1 if l1 is not None else l2
            return head.next

        res = None
        for i in range(len(lists)):
            res = merge_two_lists2(res, lists[i])
        return res


if __name__ == "__main__":
    node1 = ListNode(6)
    node2 = ListNode(6, node1)
    node3 = ListNode(5, node2)
    node4 = ListNode(4, node3)
    node5 = ListNode(3, node4)
    node6 = ListNode(3, node5)
    node7 = ListNode(2, node6)
    node8 = ListNode(1, node7)

    node10 = ListNode(2)
    node9 = ListNode(1, node10)
    lists = [node9, node8]
    solution = Solution()
    head = solution.mergeKLists([[]])
    while head:
        print(head.val)
        head = head.next

