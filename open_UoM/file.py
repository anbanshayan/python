fhandle=open("myfile.txt","w")
mystring="Python is easy. \n It's easy to learn"
fhandle.write(mystring)
#fhandle.close()
#fcontents=fhandle.read()
#read() is used to read files()
#print(fcontents)
print(fhandle.read())