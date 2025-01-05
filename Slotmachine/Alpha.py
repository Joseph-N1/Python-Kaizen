import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 # Reel count and number of reels
COLS = 3

symbol_count = { # These are the values in one reel(column) in the slot machine, they can be customize to anything you prefer,i.e anime character names, e.t.c
    "GOJO": 2,
    "YUTA": 4,
    "MEGUMI": 6,
    "YUGI": 8
}

symbol_value = {
    "GOJO": 5,
    "YUTA": 4,
    "MEGUMI": 3,
    "YUGI": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == column[line] for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = [] #Defines the column list. (Currently empty list). Remember every interior list produces the value of the items inside our column.
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # [:] the slice operator is used to create a copy and avoid a reference here. It is also a cruical step.
        for _ in range(rows):  #Loops through the number of values to be generated which is equivalent to the number of rows in the slot machine.
            value = random.choice(current_symbols) # Picks a random value
            current_symbols.remove(value) #This removes the value from the list so it is not picked again.
            column.append(value) # Adds the value to the column
        columns.append(column)
    return columns

def print_slot_machine(columns): #TRANSPOSING 
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # enumerate to find the index of the symbols to know their position
            if i != len(columns) - 1:  #This is the maximum index (lenght -1)
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():  # Collect user input , deposit and bet
    while True:
        amount = input("What would you like to deposit? £")
        if amount.isdigit():  # Checks if amount is a valid whole number
            amount = int(amount)
            if amount > 0: # Checks if amount is greater than 0
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-{}): ".format(MAX_LINES)) # Added MAX_LINES as a string because the variable involses adding two strings.
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: # Checks if amount the user is betting is within given the MAXIUMUM and MINIMUM required
                return amount
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.") # Using the f and {} helps convert variable to a string if it can be converted.
        else:
            print("Please enter a number.")

def spin(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
        print(f"You do not have enough to bet that amount, your current balance is: £{balance}")
        return 0  # No change to balance

    print(f"You are betting £{bet} on {lines} lines. Total bet is £{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press Enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
        print(f"Ending balance is £{balance}")

if __name__ == "__main__":
    main()
