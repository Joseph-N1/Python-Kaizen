# Slot Machine Project

This project is part of my Python learning journey on the Mimo app. It is designed to implement and practice Python coding skills through a fun slot machine simulation.

## How to Run

- Make sure Python is installed on your system.
- Run the script using a command line tool:


## Features

- Simple command-line interface
- Randomized slot outcomes
- Reward system based on the results

## Key Concepts Utilized
This project employs several foundational Python concepts including:

-Loops: Managing repeated execution of code blocks.
-Functions: Organizing code into reusable blocks.
-Conditional Statements: Making decisions within the code.
-Lists and Dictionaries: Managing collections of items and key-value pairs.
-User Input Handling: Capturing and validating user inputs.
-Random Number Generation: Simulating the random outcomes of a slot machine.

## Detailed Code Explanation
Loops
-Loops are a crucial part of this project as they allow us to repeat operations, such as spinning the slot machine multiple times or validating user input. Here's a breakdown of how loops are used:

  *Creating the Slot Machine Spin:
Originally, the get_slot_machine_spin function had nested loops incorrectly placed, causing premature returns and improper column handling. After restructuring:

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns



In this fixed version, the outer loop correctly iterates over each column, and the inner loop fills each column with values selected from a shuffled list of symbols.



## Issues and Fixes
-Check Winnings Function Issue:
  *The original version used a misplaced variable and loop structure that failed to correctly identify winning lines. The corrected function uses a single loop with a conditional statement to check if all symbols in a line match, significantly simplifying the logic and improving reliability.

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == column[line] for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

This correction ensures that winnings are accurately calculated and reported.


## Future Plans

-Front-End Development: Plan to develop a graphical user interface (GUI) using libraries such as Tkinter or developing a web-based interface using HTML, CSS, and JavaScript to make the game interactive and visually appealing.
-Game Features Expansion: Intend to add more features like saving high scores, multiple user support, and more advanced betting systems.


