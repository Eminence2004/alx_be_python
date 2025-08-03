# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a new bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the given amount into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the given amount if sufficient funds are available.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
