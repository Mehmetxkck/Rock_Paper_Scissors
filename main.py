import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)  # Use random.choice() to select a single choice
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You Win!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You Lose!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
