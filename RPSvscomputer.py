from random import randint


print("Welcome to the Ultimate Rock, Paper, Scissors Game \n I hope you are ready \n...ROCK...\n...PAPER...\n...SCISSORS...")
Player1 = input("(enter Player 1's choice):")
Player2 = randint(1,3)
print("Shoot!!!!")
1 is "rock"
2 is "scissors"
3 is "paper" 
if Player1 == Player2: 
        print("You guys are evenly matched , Its a tie")
elif Player1 == "rock": 
    if Player2 == "scissors":
        print("Player 1 wins")
    elif Player2 == "paper":
        print("Player 2 wins")
elif Player1 == "paper": 
    if Player2 == "scissors":
        print("Player 2 wins")
    elif Player2 == "rock":
        print("Player 1 wins")  
elif Player1 == "paper": 
    if Player2 == "scissors":
        print("Player 2 wins")
    elif Player2 == "rock":
        print("Player 1 wins") 

else: print("Something went wrong")