class A:
    def m1(self):
        print("method m1 is in class A")
class B:
    def m2(self):
        print("method m2 is in class B")
class C(B,A):
    def m3(self):
        print("method m3 is in class C")
obj=C()
obj.m1()
obj.m3()
obj.m1()
