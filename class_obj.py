class laptop:
    price=0
    processor=""
    ram=""

    def __init__(self):
        self.price=0
        self.processor=0
        self.ram=0

    def display(self):
        print("Price of the model is Rs.",self.price)
        print("Processor of the model is ",self.processor)
        print("RAM of the model is ",self.ram)

hp=laptop()
dell=laptop()

hp.price=60000
hp.processor="i7"
hp.ram="8GB"

dell.price=50000
dell.processor="i5"
dell.ram="4GB"

hp.display()
dell.display()
