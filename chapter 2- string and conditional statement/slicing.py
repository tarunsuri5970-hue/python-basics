str = "tarun"
access = str[2:4]  # we can access the element 2 and 3 only, 4th is not included
print(access)

str = "tarun"
access = str[1:len(str)]  # we can access the element 1 to length of string.
print(access)             # or we use [1: ]

str = "tarun"
access = str[ :4]       # in accessing if we dont asing the first index then automatically initialise with 
print(access)             

str = "apple"
access = str[-3:-1]    # negative index.... it start from the end of the string
print(access)           # and its index start with -1,-2,-3,-4,-5.......