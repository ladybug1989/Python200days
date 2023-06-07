print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. You have two choices "wait " or "swim" ').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which one do you choose ? ").lower()
        if choice3 == "red":
            print("Game Over, house is on fire.  ")
        elif choice3 == "yellow":
            print("You won, you got treasure. ")
        elif choice3 == "blue":
            print("You lost, beasts have come to eat you. No survival.")
        else:
             print("You chose a door that does not exist. ")
    else:
        print("You got attacked by an angry shark, hungry.. Game Over.")
else:
    print("You fell in a hole, game over.")
