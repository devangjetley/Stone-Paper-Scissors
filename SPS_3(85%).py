# Stone Paper Scissors

import random

while True:
    try:

        user_input = int(input("Press 1 for Stone | Press 2 for Paper | Press 3 for Scissors: "))   # Takes input from the user.

        system = random.randint(1, 3)       # Generates random number between 1 - 3.

        if user_input not in [1, 2, 3]:     # If user enters a number greater than 4.
            print('Invalid Input. Please, Press 1 for Stone | Press 2 for Paper | Press 3 for Scissors')
            continue
        
        def game_condition(user_input, system):
            """This function checks condition and prints result accordingly."""

            win = [(2,1), (1,3), (3,2)] # This list stores condtions in which user wins.
            lose = [(1,2), (3,1), (2,3)]    # This list stores condtions in which user loses.

            if (user_input, system) in win:
                print(f"You Entered: {user_input} | System Choose: {system}\nYou Won!!")
            elif (user_input, system) in lose:
                print(f"You Entered: {user_input} | System Choose: {system}\nYou Lose.")
            else:
                print(f"You Entered: {user_input} | System Choose: {system}\nIt's Draw.")

        
        game_condition(user_input, system)

        choice = input("Do you want to play again?(y/n): ").lower() # Whether user want to play again(IN LOWER CASE).

        match choice:   # Match-Case.
            case "n":
                break

    except ValueError:  # Handles invalid input entered by the user.
        print('Invalid Input. Please, Press 1 for Stone | Press 2 for Paper | Press 3 for Scissors') 