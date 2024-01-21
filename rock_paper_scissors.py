import random

win = [("scissors","paper"), ("paper","rock"), ("rock","scissors")]

print("There are 3 rounds.\nYou are playing against Computer.\nYou will win if you have a higher point.\nEnter scissors, paper, rock.\n")

choices = ["scissors", "paper", "rock"]

count = 0
playerPoints = 0
computerPoints = 0

while count != 3:
    player = input("What is your move? ")
    computer = random.choice(choices)
    #print(computer)

    if player != computer:
        playerWins = (player,computer)
        computerWins = (computer,player)
        if playerWins in win:
            if playerWins == win[0]:
                print("Scissors cuts paper \nYou Won!")
            elif playerWins == win[1]:
                print("Paper covers rock \nYou Won!")
            elif playerWins == win[2]:
                print("Rock crushes scissors \nYou Won!")
            playerPoints += 1
        elif computerWins in win:
            if computerWins == win[0]:
                print("Scissors cuts paper \nComputer Wins!")
            elif computerWins == win[1]:
                print("Paper covers rock \nComputer Wins!")
            elif computerWins == win[2]:
                print("Rock crushes scissors \nComputer Wins!")
            computerPoints += 1
        else:
            print("Invalid response \nComputer Wins!")
            computerPoints += 1

    elif player == computer:
        print("Draw, Player and Computer gets 1 point")
        playerPoints += 1
        computerPoints += 1

    print("")

    count += 1

if playerPoints > computerPoints:
    print("You Won :)")
elif playerPoints == computerPoints:
    print("It\'s a tie")
else:
    print("Computer Won, you lost :(")
