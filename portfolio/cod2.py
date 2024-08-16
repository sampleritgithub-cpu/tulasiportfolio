import random
choices = ["rock", "paper", "scissors"]
while True:
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice (1-3): "))
    if choice >3:
        print("Invalid choice. Please enter a number between 1 and 3.")
        continue
    user_choice = choices[choice - 1]
    print("You chose:", user_choice)
    comp_choice = random.choice(choices)
    print("Computer chose:", comp_choice)
    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")
