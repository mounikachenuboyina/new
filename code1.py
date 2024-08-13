import random

options = ["Rock", "Paper", "Scissors"]

# Get user choice and convert it to title case to handle case insensitivity
user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()

# Validate user input
if user_choice not in options:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")
else:
    # Generate computer choice
    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")
