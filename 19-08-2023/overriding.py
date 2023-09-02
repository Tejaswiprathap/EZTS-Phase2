class A:
    def m1(self):
        print("method m1 in class A")
    def m2(self):
        print("Method m2 in class A")
class B:
    def m1(self):
        print("method m1 in class B")
    def m2(self):
        print("Method m2 in class B")
obj_a=A()
obj_b=B()
for i in (obj_a,obj_b):
    i.m1()
    i.m2()
