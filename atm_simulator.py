"""
Simple ATM Simulator
--------------------
Features:
  - PIN-based login (3 attempts)
  - Check balance, deposit, withdraw
  - One function for each operation
"""

CORRECT_PIN = "1234"      # demo PIN (change it if you like)
MAX_ATTEMPTS = 3
balance = 5000.0          # starting balance


def login():
    """Ask for the PIN. Returns True if login succeeds, False otherwise."""
    for attempt in range(1, MAX_ATTEMPTS + 1):
        pin = input("Enter your 4-digit PIN: ").strip()
        if pin == CORRECT_PIN:
            print("\nLogin successful. Welcome!\n")
            return True
        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Wrong PIN. {remaining} attempt(s) left.")
    print("Too many wrong attempts. Card blocked.")
    return False


def get_amount(prompt):
    """Read a positive number from the user. Returns None if input is invalid."""
    try:
        amount = float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero.")
        return None
    return amount


def check_balance():
    """Show the current balance."""
    print(f"Your current balance is: Rs. {balance:.2f}")


def deposit():
    """Add money to the account."""
    global balance
    amount = get_amount("Enter amount to deposit: Rs. ")
    if amount is None:
        return
    balance += amount
    print(f"Rs. {amount:.2f} deposited successfully.")
    check_balance()


def withdraw():
    """Take money out of the account if enough balance is available."""
    global balance
    amount = get_amount("Enter amount to withdraw: Rs. ")
    if amount is None:
        return
    if amount > balance:
        print("Insufficient balance.")
        return
    balance -= amount
    print(f"Rs. {amount:.2f} withdrawn successfully.")
    check_balance()


def show_menu():
    """Print the ATM menu."""
    print("\n------ ATM MENU ------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def main():
    print("===== Welcome to the Simple ATM =====")
    if not login():
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
