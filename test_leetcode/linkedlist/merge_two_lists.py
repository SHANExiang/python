

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        elif l1.val >= l2.val:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2
        else:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1

    def merge_two_lists2(self, l1: ListNode, l2: ListNode) -> ListNode:
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


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)
    head = solution.merge_two_lists2(l1, l2)
    while head.next:
        print(head.val)
        head = head.next
        if head.next is None:
            print(head.val)



