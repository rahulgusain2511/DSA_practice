# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None



#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
     #Your code here
    slow=head
    fast=head
    c=0
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            c=1
            slow=slow.next
            while slow!=fast:
                c+=1
                slow=slow.next
            return c
    return 0