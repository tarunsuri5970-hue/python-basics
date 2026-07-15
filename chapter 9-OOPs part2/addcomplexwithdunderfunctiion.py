# class complex:
#     def __init__(self,real,imaginary):
#         self.real=real
#         self.imaginary=imaginary
#     def number(self):    
#         print(self.real,"i +", self.imaginary,"j")

#     def __add__(self,num2):             #dunder function.
#         newreal = self.real+num2.real
#         newimaginary = self.imaginary+num2.real
#         return  complex(newreal,newimaginary)
# num1 = complex(1, 3)
# num1.number()
# num2 = complex(4, 6)
# num2.number()
# num3 = num1+num2
# num3.number()
