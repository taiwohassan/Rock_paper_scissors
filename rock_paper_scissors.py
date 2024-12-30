import random
# Importing the `random` module to generate random choices for the computer.

user_wins = 0
computer_wins = 0
# Initializing counters to keep track of the user's and computer's wins.

options = ["rock", "paper", "scissors"]
# Defining the possible options for the game.

while True:
    # A loop that runs until the user decides to quit the game.
    
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    # Taking user input, converting it to lowercase for consistent comparison.
    
    if user_input == "q":
        # If the user types 'q', exit the loop and end the game.
        break
    
    if user_input not in options:
        # If the user input is not a valid option, skip the current iteration.
        continue
    
    random_number = random.randint(0, 2)
    # Generating a random number between 0 and 2 to determine the computer's choice.
    # rock: 0, paper: 1, scissors: 2 (mapping options to indices)
    
    computer_pick = options[random_number]
    # Selecting the computer's choice based on the random number.
    print("Computer picked", computer_pick + ".")
    # Printing the computer's choice.

    if user_input == "rock" and computer_pick == "scissors":
        # User wins if they pick "rock" and the computer picks "scissors".
        print("You won!")
        user_wins += 1
        # Incrementing the user's win counter.
        
    elif user_input == "paper" and computer_pick == "rock":
        # User wins if they pick "paper" and the computer picks "rock".
        print("You won!")
        user_wins += 1
        # Incrementing the user's win counter.

    elif user_input == "scissors" and computer_pick == "paper":
        # User wins if they pick "scissors" and the computer picks "paper".
        print("You won!")
        user_wins += 1
        # Incrementing the user's win counter.
        
    else:
        # In all other cases, the computer wins.
        print("You lost!")
        computer_wins += 1
        # Incrementing the computer's win counter.

print("You won", user_wins, "times.")
# Printing the total number of games the user won.

print("The computer won", computer_wins, "times.")
# Printing the total number of games the computer won.

print("Goodbye!")
# Printing a farewell message when the user exits the game.
