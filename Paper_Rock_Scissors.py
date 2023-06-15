import random

user_choice = int(input("Rock, paper, scissors? 0 for rock, 1 for paper and 2 for scissors ?  "))
if user_choice >= 3 or user_choice < 0:
    print(" You typed an invalid number, you lose. ")
else:
    print("Hello begin, shall we. ")
    computer_choice = random.randint(0, 2)
    print(f"computer chose {computer_choice}")
    if user_choice == 0 and computer_choice == 2:
        print("User wins !! ")
    elif computer_choice > user_choice:
        print("You lose !!! ")
    elif user_choice > computer_choice:
        print("You win !! ")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose !! ")
    elif computer_choice == user_choice:
        print("It  is a draw.  ")
    else:
        print("You print an invalid, number you lose. ")
