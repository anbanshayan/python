class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno

    def display(self):
        print("Staff's name :",self.name)
        print("Staff's regno :",self.regno)

t1=teacher("Dr.Atukorale","UCSC/01")
t2=teacher("Dr.Kasun","UCSC/02")

t1.display()
t2.display()