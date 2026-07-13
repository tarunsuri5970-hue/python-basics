f = open("Demo.txt","r")
data = f.read()   # read entire data of file
print(data)
print(type(data))
f.close()