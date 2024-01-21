import random

win = [("scissors","paper"), ("paper","rock"), ("rock","lizard"),
       ("lizard","Spock"), ("Spock","scissors"), ("scissors","lizard"),
       ("lizard","paper"), ("paper","Spock"), ("Spock","rock"),
       ("rock","scissors")]

print("There are 3 rounds.\nYou are playing against Computron.\nYou will win if you have a higher point.\nEnter scissors, paper, rock, lizard or Spock.\n")

choices = ["scissors", "paper", "rock", "lizard", "Spock"]

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
                print("Rock crushes lizard \nYou Won!")
            elif playerWins == win[3]:
                print("Lizard poisons Spock \nYou Won!")
            elif playerWins == win[4]:
                print("Spock smashes scissors \nYou Won!")
            elif playerWins == win[5]:
                print("Scissors decapitates lizard \nYou Won!")
            elif playerWins == win[6]:
                print("Lizard eats paper \nYou Won!")
            elif playerWins == win[7]:
                print("Paper disproves Spock \nYou Won!")
            elif playerWins == win[8]:
                print("Spock vapourizes rock \nYou Won!")
            elif playerWins == win[9]:
                print("Rock crushes scissors \nYou Won!")
            playerPoints += 1
        elif computerWins in win:
            if computerWins == win[0]:
                print("Scissors cuts paper \nComputron Wins!")
            elif computerWins == win[1]:
                print("Paper covers rock \nComputron Wins!")
            elif computerWins == win[2]:
                print("Rock crushes lizard \nComputron Wins!")
            elif computerWins == win[3]:
                print("Lizard poisons Spock \nComputron Wins!")
            elif computerWins == win[4]:
                print("Spock smashes scissors \nComputron Wins!")
            elif computerWins == win[5]:
                print("Scissors decapitates lizard \nComputron Wins!")
            elif computerWins == win[6]:
                print("Lizard eats paper \nComputron Wins!")
            elif computerWins == win[7]:
                print("Paper disproves Spock \nComputron Wins!")
            elif computerWins == win[8]:
                print("Spock vapourizes rock \nComputron Wins!")
            elif computerWins == win[9]:
                print("Rock crushes scissors \nComputron Wins!")
            computerPoints += 1
        else:
            print("Invalid response \nComputron Wins!")
            computerPoints += 1

    elif player == computer:
        print("Draw, Player and Computron gets 1 point")
        playerPoints += 1
        computerPoints += 1

    print("")

    count += 1

if playerPoints > computerPoints:
    print("You Won :)")
elif playerPoints == computerPoints:
    print("It\'s a tie")
else:
    print("Computron Won, you lost :(")
