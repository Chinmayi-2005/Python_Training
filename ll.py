class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=node(20)
head.next=node(21)
head.next.next=node(22)
head.next.next.next=node(23)
head.next.next.next.next=node(24)
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
#print(temp.data)     