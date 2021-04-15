class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
node1=Node(10)
class LinkedList:
    def __init__(self):
        self.head=None
    def add_begin(self,data):
        self.data=data
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_last(self,data):
        self.data=data
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            
        else:
            n=self.head
            while n is None:
                n=n.ref
            n.ref=new_node
    def print_link(self):
        
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while(n):
                print(n.data)
                n=n.ref
        
                

    

        