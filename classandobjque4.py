class cal:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    # def add(self):
    #     print("add",a+b)
    #       the reason for that we can't put like a+b as above scenerio is a,b are not defined in above function (add function). So we can use the assigned variables for self instead of using not degined a,b at this instance.
    

    def add(self):
        print("add",self.num1,self.num2)
    
    # def subtract(self,a,b):
    #     return a-b
    
    # def multiply(self,a,b):
    #     return a*b
    
    # def divide(self,a,b):
    #     return a/b
    
val1=cal(56,44)
val1.add()
    
