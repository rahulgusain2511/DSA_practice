class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    pos=0
    n=head
    while n is not None:
        if pos==p:
            
            break
        pos=pos+1
        n=n.next
    new_node=Node(data)
    new_node.next=n.next
    
    new_node.prev=n
    n.next=new_node

    