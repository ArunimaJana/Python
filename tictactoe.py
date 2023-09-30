choices,x,o=0,0,0
choices= [1,2,3,4,5,6,7,8,9]
#This function is displaying the board of tictactoe
def display_board():
    print(choices[0]," |",choices[1],"| ",choices[2])
    print("___|___|___")
    print(choices[3]," |",choices[4],"| ",choices[5])
    print("___|___|___")
    print(choices[6]," |",choices[7],"| ",choices[8])
#To take input from player 1    
def player1():
    x=int(input("Enter your choice:"))
    choices[x-1]="X"
#To take input from player 2    
def player2():
    o=int(input("Enter your choice:"))
    choices[o-1]="O"
#Check if the cell is occupied
def checkcell():
    if(choices[x-1]!="X" or choices[o-1]!="O"):
        player2()
        
    else:
        print("Cell is occupied choose another cell")
#checking win/draw
def checkwin():
    if(choices[0]=="X" and choices[0]==choices[1] and choices[1]==choices[2]):  
        print("Player 1 won")
    elif(choices[3]=="X" and choices[3]==choices[4] and choices[4]==choices[5]): 
        print("Player 1 won")    
    elif(choices[6]=="X" and choices[6]==choices[7] and choices[7]==choices[8]): 
        print("Player 1 won")
    elif(choices[0]=="X" and choices[0]==choices[3] and choices[3]==choices[6]):
        print("Player 1 won")
    elif(choices[1]=="X" and choices[1]==choices[4] and choices[4]==choices[7]):
        print("Player 1 won")
    elif(choices[2]=="X" and choices[2]==choices[5] and choices[5]==choices[8]):
        print("Player 1 won")
    elif(choices[0]=="X" and choices[0]==choices[4] and choices[4]==choices[9]):
        print("Player 1 won")
    elif(choices[2]=="X" and choices[2]==choices[4] and choices[4]==choices[6]):
        print("Player 1 won")
    elif(choices[0]=="O" and choices[0]==choices[1] and choices[1]==choices[2]):
        print("Player 2 won")
    elif(choices[3]=="O" and choices[3]==choices[4] and choices[4]==choices[5]):
        print("Player 2 won")    
    elif(choices[6]=="O" and choices[6]==choices[7] and choices[7]==choices[8]):
        print("Player 2 won")
    elif(choices[0]=="O" and choices[0]==choices[3] and choices[3]==choices[6]):
        print("Player 1 won")
    elif(choices[1]=="O" and choices[1]==choices[4] and choices[4]==choices[7]):
        print("Player 1 won")
    elif(choices[2]=="O" and choices[2]==choices[5] and choices[5]==choices[8]):
        print("Player 1 won")
    elif(choices[0]=="O" and choices[0]==choices[4] and choices[4]==choices[9]):
        print("Player 1 won")
    elif(choices[2]=="O" and choices[2]==choices[4] and choices[4]==choices[6]):
        print("Player 1 won")
    else:
        print("Draw")
i=0                       
while(i<9):
    display_board()
    player1()
    display_board()
    player2()
    checkcell()
    checkwin()
    i=i+1


