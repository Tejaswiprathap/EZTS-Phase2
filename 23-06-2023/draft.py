'''you are given a circular linked list ,but you suspect that it might contain a loop. a loop occurs when a node's next pointer
points to a node that has been visited before in the traversal.your task is to
write a function detect_loop that detects if a loop exists in the circular linked list.'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_beg(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
    def detect_loop():
        if tail.next==head.next:
            print("it has a loop ")
        else:
            print("it does not have a loop")
    def display(self):
        if self.head is None:
            print("Circular Linked list is empty")
        else:
            temp=self.head #temp=first node
            print(temp.data,end=" -> ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,end=" -> ")
                
            print(temp.next.data)
            #temp.data means first node's data
    def detect_loop(self
                    ):
        if self.tail.next==self.head:
            print("it has a loop ")

obj=cll()
node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node5=node(50)
node6=node(60)
obj.head=node1
obj.tail=node1
obj.tail.next=obj.head
#print(obj.tail.next)
node1.next=node2
obj.tail=node2
obj.tail.next=obj.head
#print(node1.next)
#print(obj.tail.next)
#print(node2.next)
node2.next=node3
obj.tail=node3
obj.tail.next=obj.head
#print(obj.tail.next)
node3.next=node4
obj.tail=node4
obj.tail.next=obj.head
#print(obj.tail.next)
node4.next=node5
obj.tail=node5
obj.tail.next=obj.head
#print(obj.tail.next)
node5.next=node6
obj.tail=node6
obj.tail.next=obj.head
#print(obj.tail.next)
obj.display()
print()
obj.insert_beg(70)
obj.display()
obj.detect_loop()
