## question1
# f = open("practice.txt","w")
# f.write("Hi everyone\nwe are learning file I/O\nusing java.\ni like programming in java")

#question2
f = open("practice.txt","r")
data = f.read()

new_data=data.replace("java","python")
print(new_data)

f = open("practice.txt","w")
f.write(new_data)