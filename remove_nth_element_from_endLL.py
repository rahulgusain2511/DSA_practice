# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
      
        
        h=c=head
        cnt=0
        while h is not None:
            cnt+=1
            h=h.next

        if cnt == n:
            head = head.next
            return head
        
        pos=0
        while c is not None:
            if pos==cnt-n-1:
                break
            pos+=1
            c=c.next
        
        c.next=c.next.next
        return head