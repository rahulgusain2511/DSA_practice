# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        arr=[]
        n=head
        c=head
        while n is not None:
            arr.append(n.val)
            n=n.next
        arr.reverse()
        p=ListNode(arr[0])
        m=p
        for i in arr[1:]:
            node = ListNode(i)
            m.next = node
            m = node
        return p

