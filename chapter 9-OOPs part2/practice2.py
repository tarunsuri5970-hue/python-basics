# # question 1 
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
# # to calculate area 
#     def area(self):
#         return (self.radius*self.radius*3.14)
# # to calculate parameter   
#     def parameter(self): 
#         return 2*self.radius*self.radius*3.14

# c1 = circle(5)

# print("area:",c1.area())


# question 2
class employe:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def detail(self):
        print("role:",self.role)
        print("department:",self.dept)
        print("salery:",self.sal)

class engineer(employe):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT","70000")
engg1 = engineer("taurn",23)
engg1.detail()
