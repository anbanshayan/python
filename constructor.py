#Constructors and self keyword
class laptop:
    def __init__(self):
        self.price=0
        self.processor=""
        self.RAM=""
    def display(self):
        print("Price :",self.price)
        print("RAM :",self.RAM)
        print("Processor :",self.processor)

hp=laptop()
dell=laptop()
lenevo=laptop()

hp.price=178000
hp.processor="i9"
hp.RAM="32GB"

dell.price=168000
dell.processor="i7"
dell.RAM="16GB"

lenevo.price=178000
lenevo.processor="i5"
lenevo.RAM="8GB"

print("HP")
hp.display()

print("DELL")
dell.display()

print("Lenevo")
lenevo.display()