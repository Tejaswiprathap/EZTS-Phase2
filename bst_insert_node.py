class node:
    def __init__(self,data):
        self.lchild=None
        self.data=data
        self.rchild=None
class bst:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert_node(self,data):
        if self.key is None:
            print("empty")
            return
        if self.key==data:
            print("data element is already present")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert_node(data)
            else:
                self.lchild=bst(data)
        else:
            if self.rchild:
                 self.rchild.insert_node(data)
            else:
                
                self.rchild=bst(data)
            
root=bst(45)
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
n6=node(60)
n7=node(70)
#obj.root=n1
'''print(obj.root)
print(n1)'''
#print(n1.rchild)
n1.rchild=n2
n1.lchild=n3
n2.lchild=n4
n2.rchild=n5
n3.lchild=n6
n3.rchild=n7 
root.insert_node(10)
root.insert_node(20)
root.insert_node(30)
root.insert_node(40)
root.insert_node(50)
root.insert_node(60)
root.insert_node(70)
root.insert_node(80)
root.insert_node(90)
root.insert_node(100)
