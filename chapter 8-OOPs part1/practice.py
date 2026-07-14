# creat student class that takes name and marks  of 3 subject as argument in constructor.
# then create a method to print the average.
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your average marks is :",sum/3)


s1 = student("tarun",[78,89,67])
s1.average()
             