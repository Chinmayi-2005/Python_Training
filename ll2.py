class Node:
    def __init__(self,data):
    
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def appened(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        print("none")
l1=linkedlist()
l1.appened(1)
l1.appened(2)
l1.appened(3)
l1.display()