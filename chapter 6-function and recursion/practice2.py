# # write a recursive function to calculate the sum of first n natural number.
# def sum(n):
#     if (n==0):
#         return 0
#     return n + sum(n-1)
    
# print(sum(5))

# write a recursive function to print all element in a list.
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits = ["mango","banana","kela","apple"] 
print_list(fruits)  
