# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow=fast=entry=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                while slow!=entry:
                    entry=entry.next
                    slow=slow.next
                return entry
        return None