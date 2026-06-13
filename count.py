class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def appened(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next   
        temp.next=new_node
    def count(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        print(c)

l=linkedlist()
for i in range(6):
    l.appened(i)
l.count()
