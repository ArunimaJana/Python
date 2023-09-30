#import random
import sys
import getpass
#n = random.randrange(1,10)
print("Hi! Welcome to number guessing game")

# print("So here are the instructions:\nYou will get three turns to guess the right number")
# print("Machine has already chosen. It is your turn.")
# print("Let me help you a bit choose between 1 to 10")
n=int(getpass.getpass(prompt="Enter a number between 1 to 20 :: ",stream=None))
if n>20:
    print("Choose between 1 to 20")
    sys.exit()
guess = int(input("Enter: "))
i=1
while i!=4:
    if n==guess :
        print("Congratulations you win!!!")
        sys.exit()
    elif n<guess and i==1:
        print("Let me give you another hint :)")
        print("Guess lower") 
        guess = int(input("Guess again: "))  
    elif n>guess and i==1:
        print("Let me give you another hint :)")
        print("Guess higher") 
        guess = int(input("Guess again: "))
    elif n%2==0 and i==2:
        print("Let me give you a hint >_<")
        print("The number is even") 
        guess = int(input("Guess again: "))  
    elif n%2!=0 and i==2:
        print("Let me give you a hint >_<")
        print("The number is odd") 
        guess = int(input("Guess again: "))      
    i+=1 
print("Sorry you lost *_*")