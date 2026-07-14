class student:

    def __init__(self,fullname,marks):    
        self.name = fullname        
        self.marks = marks         
    
    def welcome(self):
        print("welcome student",self.name)
       
    def getmarks(self):
        return self.marks
s1 = student("karan",78)
s1.welcome()
print(s1.getmarks())      