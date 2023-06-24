class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__(self):
        self.head=None
n1=Node("varshi")
'''print(n1)
print(n1.data)'''
n2=Node("teju")
'''print(n2)
print(n2.prev)'''
n3=Node("shashi")
n4=Node("mani")
n5=Node("vishnu")
n1.next=n2
n2.prev=n1
print(n2.data)
print(n2.prev)
n2.next=n3
n3.prev=n2
print(n3.data)
print(n3.prev)
print(n2.next)
