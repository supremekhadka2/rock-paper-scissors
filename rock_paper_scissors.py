import random

users_wins = 0
computers_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    elif user_input not in ["rock", "paper", "scissors"]:
        continue 
        
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("\nCompter picked", computer_pick + ".")

    if user_input == computer_pick:
        print("Draw!")

    elif user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        users_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        users_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
         print("You Won")
         users_wins += 1

    else:
        print("Computer Won!")
        computers_wins += 1

print("\nYou won", users_wins, "times.")
print("Computer won", computers_wins, "times.")
print("Goodbye!")