class Fruit:

    def __init__ (self):
        self.name=""
        self.color=""

    def display(self):
        print("Name of the fruit :",self.name)
        print("Color of the fruit :",self.color)

apple=Fruit()

apple.name="Apple"
apple.color="Red"

apple.display()


