# Simple ATM Simulator (Python)

A command-line ATM simulator built as a Week 1 mini project. It lets a user log in with a PIN and then check their balance, deposit money, or withdraw money.

## Features

- PIN-based login with 3 attempts (the card is blocked after 3 wrong tries)
- Check balance
- Deposit money
- Withdraw money, with an "Insufficient balance" check
- Input validation for invalid amounts and menu choices
- One function for each operation

## Project Structure

| Function | Purpose |
|---|---|
| `login()` | Asks for the PIN and allows up to 3 attempts |
| `check_balance()` | Shows the current balance |
| `deposit()` | Adds money to the balance |
| `withdraw()` | Deducts money if enough balance is available |
| `get_amount()` | Reads and validates an amount entered by the user |
| `show_menu()` | Prints the ATM menu |
| `main()` | Runs the program loop |

## How to Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download `atm_simulator.py`.
3. Open a terminal in the same folder and run:

```
python atm_simulator.py
```

**Demo PIN:** `1234`
**Starting balance:** Rs. 5000

## Sample Output

```
===== Welcome to the Simple ATM =====
Enter your 4-digit PIN: 1234

Login successful. Welcome!

------ ATM MENU ------
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Choose an option (1-4): 2
Enter amount to deposit: Rs. 500
Rs. 500.00 deposited successfully.
Your current balance is: Rs. 5500.00
```

## Concepts Used

- Functions
- Loops and conditionals
- Input validation with `try`/`except`
- Global variables

## Possible Improvements

- Save the balance to a file so it persists between runs
- Add a transaction history
- Add a change-PIN option

## Author

Anshika Khewariya
