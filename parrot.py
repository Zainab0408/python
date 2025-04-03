class parrot:
    species="bird"
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
coco=parrot("coco",2)
floof=parrot("floof",1)
coco.printinfo()
coco.sing("happy note")
coco.dance()
floof.printinfo()
floof.sing("happy note")
floof.dance()
