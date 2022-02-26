import random

choices = ["Rock", "Paper", "Scissors"]
player = False
computer_score = 0
player_score = 0

while True:
    player = input("Rock, Paper or Scissors? ").capitalize()
    computer_choice = random.choice(choices)
    if player == computer_choice:
        print("Tie!")
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You lose!", computer_choice, "covers", player)
            computer_score += 1
        else:
            print("You win", player, "Smashes", computer_choice)
            player_score += 1
    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You lose", computer_choice, "cuts", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer_choice)
            player_score += 1
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "Smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cuts the", computer_choice)
            player_score += 1
    elif player == "End":
        print("Final Scores are:")
        print(f"Player: {player_score}")
        print(f"Computer Score: {computer_score}")
        break
