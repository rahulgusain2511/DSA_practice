
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        n=len(arr)
        if(n==0):
            return None
        self.head=Node(arr[0])
        p=self.head
        for i in range(1,n):
            p.next=Node(arr[i])
            p.next.prev=p
            p=p.next
        return self.head