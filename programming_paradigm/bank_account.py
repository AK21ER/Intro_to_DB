
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds exist.
        Returns True if withdrawal was successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
