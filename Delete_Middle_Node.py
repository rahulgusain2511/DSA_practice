# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        cnt=0
        n=head
        while n is not None:
            cnt+=1
            n=n.next
        
        z=cnt
        pos=0

  
      
     
        c=head
        if c.next==None:
            return None
        while pos<(cnt//2)-1:

            pos=pos+1
   
            c=c.next
            
        c.next=c.next.next
        return head
