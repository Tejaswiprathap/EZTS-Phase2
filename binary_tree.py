class node:
    def __init__(self,data):
        self.lchild=None
        self.data=data
        self.rchild=None
class tree:
    def __init__(self):
        self.root=None

n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)
n6=node(60)
n7=node(70)
obj=tree()
obj.root=n1
'''print(obj.root)
print(n1)'''
print(n1.rchild)
n1.rchild=n2
n1.lchild=n3
n2.lchild=n4
n2.rchild=n5
n3.lchild=n6
n3.rchild=n7 
