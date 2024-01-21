import random

win = [("scissors","paper"), ("paper","rock"), ("rock","lizard"),
       ("lizard","Spock"), ("Spock","scissors"), ("scissors","lizard"),
       ("lizard","paper"), ("paper","Spock"), ("Spock","rock"),
       ("rock","scissors")]

print("There are 3 rounds.\nYou are playing against LCARS.\nYou will win if you have a higher point.\nEnter scissors, paper, rock, lizard or Spock.\n")

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
                print("Scissors cuts paper \nLCARS Wins!")
            elif computerWins == win[1]:
                print("Paper covers rock \nLCARS Wins!")
            elif computerWins == win[2]:
                print("Rock crushes lizard \nLCARS Wins!")
            elif computerWins == win[3]:
                print("Lizard poisons Spock \nLCARS Wins!")
            elif computerWins == win[4]:
                print("Spock smashes scissors \nLCARS Wins!")
            elif computerWins == win[5]:
                print("Scissors decapitates lizard \nLCARS Wins!")
            elif computerWins == win[6]:
                print("Lizard eats paper \nLCARS Wins!")
            elif computerWins == win[7]:
                print("Paper disproves Spock \nLCARS Wins!")
            elif computerWins == win[8]:
                print("Spock vapourizes rock \nLCARS Wins!")
            elif computerWins == win[9]:
                print("Rock crushes scissors \nLCARS Wins!")
            computerPoints += 1
        else:
            print("Invalid response \nLCARS Wins!")
            computerPoints += 1

    elif player == computer:
        print("Draw, Player and LCARS gets 1 point")
        playerPoints += 1
        computerPoints += 1

    print("")

    count += 1

if playerPoints > computerPoints:
    print("You Won :)")
elif playerPoints == computerPoints:
    print("It\'s a tie")
else:
    print("LCARS Won, you lost :(")
