

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_Palindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def is_palindrome(self, head):
        self.front_pointer = head

        def recur(current_node=head):
            if current_node != None:
                if not recur(current_node.next):
                    return False
                if current_node.val != self.front_pointer.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        return recur(head)

    def is_palindrome2(self, head):
        if not head:
            return True
        fast_pointer = head
        slow_pointer = head

        def get_half_pointer(fast_pointer, slow_pointer):
            while fast_pointer.next and fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            return slow_pointer

        def reverse_linkedlist(head):
            pre = None
            cur = head
            while cur:
                node = cur.next
                cur.next = pre
                pre = cur
                cur = node
            return pre

        slow_pointer = get_half_pointer(fast_pointer, slow_pointer)
        slow_pointer = reverse_linkedlist(slow_pointer.next)
        while slow_pointer:
            if slow_pointer.val != head.val:
                return False
            slow_pointer = slow_pointer.next
            head = head.next
        return True
