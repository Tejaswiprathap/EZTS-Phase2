class A:
    def m1(self):
        print("method m1 is in class A")
class B(A):
    def m2(self):
        print("method m2 is in class B")
class C(B):
    def m3(self):
        print("method m3 is in class C")
obj_c=C()
obj_c.m1()
obj_c.m2()
obj_c.m3()
