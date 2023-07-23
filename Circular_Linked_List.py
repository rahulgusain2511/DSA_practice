class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Circular_Linked_List:
    def __init__(self):
        self.head=None
        self.end=None
                
    def traverse(self):
        if self.head==None:
            print("circular linked list is empty")
        else:
            n=self.head
            while n.ref:
                print(n.data,"-->",end="")
                n=n.ref
                if n==self.head:
                    break
    
    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.head.ref=new_node
            self.end=new_node
            return
        if self.end!=None:
            self.end.ref=new_node
            new_node.ref=self.head
            self.end=new_node
            return
        
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        n=self.head
        
        if n is None:
            self.head=new_node
            self.end=new_node
            self.head.ref=new_node
            return
        
        if self.end is not None:
            self.end.ref=new_node
            new_node.ref=self.head
            self.head=new_node
            return     

    def add_after(self,data,x):
        n=self.head
        while n is not self.end:
            if n.data==x:
                break
            n=n.ref 
        
        if n.data != x :
            print("node is not present in Linked List")
            return
        if n.data is self.end:
            self.insert_end
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node           
    
    def add_before(self,data,x):
        n=self.head
        if n is None:
            print("circular linked list is empty")
            return
        if n.data==x:
            self.insert_begin(data)
            return
     
        while n.ref is not self.end:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref.data != x:
            print("node not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node       
                       
    def deleteStart(self):    
            
        if(self.head == None):
            print("linked list is empty")
                
        else:    
              
            if(self.head != self.end ):    
                self.head = self.head.ref;    
                self.end.ref = self.head;    
            
            else:    
                self.head = self.end = None;      
        
    def delete_from_end(self):  
        if(self.head == None):  
            return 
        else:  
            if(self.head != self.end ):  
                n = self.head              
                while(n.ref != self.end):  
                    n = n.ref  
                self.end = n 
                self.end.ref = self.head;  
            else:  
                self.head = self.end = None;   
    def delete_any(self,x):
        if self.head is None:
            print("linked list is empty")
            return
        if x==self.head.data:
            self.deleteStart()
            return
        n =self.head
        while n.ref is not self.end:
            if x==n.ref.data:
                break
            n=n.ref    
        if n.ref.data != x:
            print("node is not present !!")
        else:
            n.ref=n.ref.ref

circularlist=Circular_Linked_List()
circularlist.insert_begin(10)
circularlist.insert_begin(20)
circularlist.insert_begin(30)
circularlist.insert_begin(40)
circularlist.insert_end(50)
circularlist.add_after(15,50)
circularlist.add_before(15,10)
circularlist.delete_start()
circularlist.delete_from_end()
circularlist.delete_any(50)
circularlist.traverse()

       
 