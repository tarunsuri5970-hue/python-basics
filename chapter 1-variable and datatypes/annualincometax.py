annualincome = float(input("enter your annual income:"))
if annualincome <=400000 :
    tax = 0
elif annualincome <=800000 :
    tax=annualincome*0.05
elif annualincome <=1200000 :
    tax=annualincome*0.1
elif annualincome <=1600000 :
    tax=annualincome*0.15
elif annualincome <=2000000 :
    tax=annualincome*0.2
elif annualincome <=2400000 :
    tax=annualincome*0.25
else:
    tax=annualincome*0.3
print("your annual income is:",annualincome)
print("your tax is:",tax)
print("your remaining income is:",(annualincome-tax))