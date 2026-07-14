class student:
    
    # defalt constructor
    def __init__(self):
        pass

    # parameterize constructor
    def __init__(self,fullname,marks):    # creating a constructor
        self.name = fullname         # varibale ( name ) is created that store fullname
        self.marks = marks           # varibale ( marks ) is created that store marks.
        print("adding new student in database")
s1 = student("karan",78)
print(s1.name,s1.marks)      # karan and marks 78
s2 = student("tarun",90)
print(s2.name,s1.marks)      # tarun and marks 90