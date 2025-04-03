class rabbit:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printinfo(self):
        print("my name is",self.name)
        print("my age is",self.age)
    def sing(self,song):
        print("{} sings a {}".format(self.name,song))
    def sing(self):
        print("{} is now dancing {}".format(self.name))
bunny=rabbit("bunny",2)
snowball=rabbit("snowball",1)
bunny.printinfo()
bunny.sing("happy note")
bunny.dance()
snowball.printinfo()
snowball.sing("happy note")
snowball.dance()
