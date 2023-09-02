class Person():
    def hello(self,name=None):
        if name is not None:
            print("hello "+name)
        else:
            print("hello")
obj=Person()
obj.hello()
obj.hello("Tejaswi ")
