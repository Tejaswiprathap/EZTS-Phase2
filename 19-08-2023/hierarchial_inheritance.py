class A:
    def m1(self):
        print("method m1 is in class A")
class B(A):
    def m2(self):
        print("method m2 is in class B")
class C(A):
    def m3(self):
        print("method m3 is in class C")
obj_a=A()
obj_b=B()
obj_c=C()
obj_c.m1()
obj_c.m3()
obj_b.m1()
