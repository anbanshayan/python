class company():
    def __init__(self):
        self.__companyName="Namasi"

    def companyName(self):
        print(self.__companyName)

c1=company()
c1.companyName()
print(c1.__companyName)