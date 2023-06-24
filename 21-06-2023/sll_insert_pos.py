class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos,data):
        ne=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        ne.next=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                if temp.next!=None:
                    print(temp.data,end=" -> ")
                else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                temp=temp.next
obj=sll()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
n6=node(70)
n5.next=n6

obj.display()
obj.insert_pos(2,'200')
print()
obj.display()
