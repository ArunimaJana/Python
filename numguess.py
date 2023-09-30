import sys
import getpass
def player1():
    n=int(getpass.getpass(prompt="Player 1-Enter a number between 1 to 20 :: ",stream=None))
    if n>20:
        print("Choose between 1 to 20")
        con()
    else:
        print("Player 1 has entered a number.")
    guess = int(input("Player 2-Try to guess it: "))
    i=1
    while i!=4:
        if n==guess :
            print("Congratulations Player 2 wins!!!")
            player2()
        elif n<guess and i==1:
            print("Let me give you a hint :)")
            print("Guess lower") 
            guess = int(input("Guess again: "))  
        elif n>guess and i==1:
            print("Let me give you a hint :)")
            print("Guess higher") 
            guess = int(input("Guess again: "))
        elif n%2==0 and i==2:
            print("Let me give you another hint >_<")
            print("The number is even") 
            guess = int(input("Guess again: "))  
        elif n%2!=0 and i==2:
            print("Let me give you another hint >_<")
            print("The number is odd") 
            guess = int(input("Guess again: "))      
        i+=1 
    print("Player 2 lost *_*")
def player2():
    n=int(getpass.getpass(prompt="Player 2-Enter a number between 1 to 20 :: ",stream=None))
    if n>20:
        print("Choose between 1 to 20")
        con()
    else:
        print("Player 1 has entered a number.")
    guess = int(input("Player 2-Try to guess it: "))
    i=1
    while i!=4:
        if n==guess :
            print("Congratulations Player 1 win!!!")
            con()
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
    print("Player 1 lost *_*")
    con()
def con():
    choice=input("Do you want to continue:")
    while choice=='yes':
        player1()
        player2()
    sys.exit()    
def display():
    print("Hi! Welcome to number guessing game")
    print("So here are the instructions:\nEach player will get three turns to guess the right number\n")
display()
player1()
player2()