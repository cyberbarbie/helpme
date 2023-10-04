from random import randint

print("Welcome to the Ultimate Rock, Paper, Scissors Game \n I hope you are ready \n...ROCK...\n...PAPER...\n...SCISSORS...")
Player1 = input("(enter Player 1's choice): ")
Player2 = randint(1, 3)
print("Shoot!!!!")

if Player1 == "rock":
    if Player2 == 1:
        print("You guys are evenly matched, It's a tie")
    elif Player2 == 2:
        print("Player 2 wins")
    elif Player2 == 3:
        print("Player 1 wins")
elif Player1 == "paper":
    if Player2 == 1:
        print("Player 1 wins")
    elif Player2 == 2:
        print("You guys are evenly matched, It's a tie")
    elif Player2 == 3:
        print("Player 2 wins")
elif Player1 == "scissors":
    if Player2 == 1:
        print("Player 2 wins")
    elif Player2 == 2:
        print("Player 1 wins")
    elif Player2 == 3:
        print("You guys are evenly matched, It's a tie")
else:
    print("Something went wrong")
