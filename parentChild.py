class Parent:
    def hello(self):
        print("This the parent body")

class child(Parent):
    def hi(self):
        print("This the child body")

class grandChild(child):
    def how(self):
        print("This the Grand child body")


mc= grandChild()
mc.hello()
mc.hi()
mc.how()
