import random

while True:
    user_action = input("Choose between rock, paper, or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock beats scissors! You win!")
        else:
            print("paper beats rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper beats rock! You win!")
        else:
            print("scissors beats paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors beats paper! You win!")
        else:
            print("rock beats scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break