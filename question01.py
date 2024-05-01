#set uname="EMC" and password = "123". Create a function 'validate' and validate them by returning true or false

uname="EMC"
password="123"

def validate(uname,password):
    if uname == "EMC" and password == "123":
        return True
    else:
        return False
    
uname=input("Enter Your Username")
password=input("Enter Your Password")

print(validate(uname,password))