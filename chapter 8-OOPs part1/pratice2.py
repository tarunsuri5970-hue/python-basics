# # creat a account class with 2 attriibutes- balance and account no.
# # creat a method  for debit , credit, printing the balance.
# class account:
#     def __init__(self,balance,accno):
#         self.balance = balance
#         self.account_number = accno
#     # debit method 
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs",amount,"was debited ")
#         print("total amount:",self.balance)

#        # credit method 
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount,"was credited")
#         print("total amount:",self.balance)

#           # credit method 
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount,"was credited")
#         print("total amount:",self.balance)

#     # final balance  
#     def final_bal(self):
#         return self.balance
        
    

# acc1 = account(10000,786)
# print("your acc no.",acc1.account_number)
# print("your previos balance no.",acc1.balance)
# acc1.debit(1000)
# acc1.credit(1500)