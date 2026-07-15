# random password generator.
import random  # use the module random (this help in generate in random number).
import string  # this import all character like (A,S,H,n,g,o,u,i,1,3,@,#,$) etc.

pass_len = 12
charvalue = string.ascii_letters + string.digits + string.punctuation   
# that variable name (charvalue) contain the all letter , digit , punctuations.
password = ""
for i in range(pass_len):
    password += (random.choice(charvalue))

print("your random password is:",password)