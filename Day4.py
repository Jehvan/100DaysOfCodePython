import random

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
comp_choice = random.randint(0, 2)
print(f"Computer chose: {comp_choice}")
game_options = ["rock", "paper", "scissors"]
if choice == comp_choice:
    print("Draw")
    print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
elif choice == 0:
    if comp_choice == 1:
        print("You lose!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
    else:
        print("You win!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
elif choice == 1:
    if comp_choice == 2:
        print("You lose!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
    else:
        print("You win!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
else:
    if comp_choice == 0:
        print("You lose!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")
    else:
        print("You win!")
        print(f"Computer chose: {game_options[comp_choice]}, you chose: {game_options[choice]}")