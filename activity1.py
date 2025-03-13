import random
c=random.randint(1,10)
print("welcome to the number guessing game")
userchoice=int(input("enter the number : "))
if userchoice==c:
    print("you win")
else:
    print("try again")
    print("computer choice : " ,c)