# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



        
class Solution(object):
    def sortList(self, head):
        if head is None:
            return None
        n=head
        c=head
        arr=[]
        while n is not None:
            arr.append(n.val)
            n=n.next
        l=len(arr)
        arr.sort()
        c=ListNode(arr[0])
        m=c
        for i in range(1,l):
            new_node=ListNode(arr[i])
            m.next=new_node
            m=new_node
        return c