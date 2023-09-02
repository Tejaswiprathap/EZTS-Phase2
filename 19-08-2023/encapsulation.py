class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def m1(self):
        print("I'm "+self.name)
        print(f"I'm {self.age} years old")
obj=Student("Tejaswi",21)
obj.m1()
