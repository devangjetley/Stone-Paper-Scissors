# Stone Paper Scissors

## Introduction

This Python script allows you to play the classic "Stone, Paper, Scissors" game against the computer.

## Features

1. **Match Case**: Utilizes match-case for cleaner and more readable code.
2. **Continuous Gameplay**: Runs continuously until the user decides to exit.
3. **Error Handling**: Handles invalid inputs gracefully.
4. **Randomization**: Uses the random module to generate a random choice for the computer.
5. **Formatted Output**: Uses f-strings for cleaner and easier-to-maintain code.

## How to Use

1. **Run the Program**: Execute the script in a Python environment.
2. **Enter Input**: Press 1 for Stone | Press 2 for Paper | Press 3 for Scissors.
3. **View Result**: The program will display whether you won, lost, or it's a draw.
4. **Continue or Exit**: You will be prompted to continue or exit the game. Enter 'y' to play again or 'n' to stop.

## Code Explanation

1. Main Loop: The script runs in a while True loop, continuously prompting the user for input.
2. Error Handling: A try-except block is used to catch ValueError exceptions if the user enters invalid input.
3. User Input: The user is prompted to enter a number (1 for Stone, 2 for Paper, 3 for Scissors).
4. Random Choice: The computer randomly selects a choice (1, 2, or 3) using random.randint.
5. Game Logic: The game_condition function checks the user's input against the computer's choice and prints the result (win, lose, or draw).
6. Replay Option: After each round, the user is asked if they want to play again. If the user enters 'n', the loop breaks and the game ends; otherwise, it continues.
