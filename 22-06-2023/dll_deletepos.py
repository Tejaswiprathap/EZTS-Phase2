class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
        temp.prev=prev
    def display(self):
        if self.head is None:
            print("Doubly linked list is empty!")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" <-> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next

obj=dll()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n2.prev=n1
n3=node(40)
n2.next=n3
n3.prev=n2
n4=node(50)
n3.next=n4
n4.prev=n3
n5=node(60)
n4.next=n5
n5.prev=n4
n6=node(70)
n5.next=n6
n6.prev=n5

obj.display()
print()
obj.delete_pos(3)
obj.display()
print()
