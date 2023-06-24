class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        new_node=node(data)
        temp=self.head
        temp.prev=new_node
        new_node.next=temp
        self.head=new_node
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
obj.insert_beg(80)
obj.display()
print()
