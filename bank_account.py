class BankAccount():
    accounts_created = 0

    def __init__(self, account_owner: str, account_number: str, account_balance: float | int = 0):
        if account_balance < 0:
            raise ValueError("Bank account balance cannot be negative")
        BankAccount.accounts_created += 1
        self.account_number = account_number
        self.account_owner = account_owner
        self._balance = account_balance

    def __repr__(self):
        return f"BankAccount({self.account_owner}, {self.account_number}, {self._balance})"

    def deposit(self, amount: float | int) -> None:
        if amount <= 0:
            raise ValueError("Amount cannot be negative")
        self._balance += amount

    def withdraw(self, amount: float | int) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds for withdrawal")
        self._balance -= amount

    def transfer_to(self, other_account: 'BankAccount', amount: float | int) -> None:
        if not isinstance(other_account, BankAccount):
            raise TypeError("Can only transfer to BankAccount instance")
        try:
            self.withdraw(amount)
            other_account.deposit(amount)
        except ValueError as e:
            raise ValueError(f"Transfer failed: {e}")

    def info(self) -> str:
        return f"Bank account: {self.account_owner}, {self.account_number}, {self._balance}"

    @classmethod
    def get_accounts_created(cls):
        return cls.accounts_created


bank_account = BankAccount(account_owner='Petr A', account_number='416515644544', account_balance=10000)
