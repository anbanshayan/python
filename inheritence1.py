class dad:
    def phone(self):
        print("Dad's phone")

class mom:
    def love(self):
        print("Mom's love")

class son(dad,mom):
    def laptop(self):
        print("Son's laptop")




child=son()
child.phone()
child.love()