class Myclass:
    __num = 10
    def add(self):
        y = self
        y.__num = 400
        print("Value of num before return" , y.__num)

mc = Myclass()
mc.add()
print("value of num after is",y.__num )
