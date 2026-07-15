# # create a game to guess a number between 1 and 100.
# import random  # use the module random (this help in generate in random number).

# target = random.randint(1,100) # return random integer in range [a,b]

# while True:
#     userChoice = (input("guess the target or Quit:"))
#     if (userChoice=="Quit"):
#         break
#     userChoice = int(userChoice)
    
#     if (userChoice == target):
#         print("success : correct guess!!")
#         break
#     elif (userChoice < target):
#         print("your guess is smaller than target. take a bigger guess...")
#     else:
#         print("your guess is bigger than target. take a smaller guess...")
# print("---GAME OVER---")
