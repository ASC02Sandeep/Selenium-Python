"""
Banking Application
"""

from abc import ABC, abstractmethod
from datetime import datetime
import json
import os
import uuid

# ===========================
# OOP PRINCIPLES OVERVIEW
# ===========================
# 1. Abstraction     -> Abstract class Account
# 2. Encapsulation   -> Private attributes with property getters/setters
# 3. Inheritance     -> SavingsAccount and CheckingAccount inherit from Account
# 4. Polymorphism    -> Withdraw() works differently in each subclass


# -----------------------
# Base Abstract Class
# -----------------------
class Account(ABC):
    """Abstract base class for all account types (Abstraction)."""

    def __init__(self, account_id: str, owner: str, balance: float = 0.0):
        self._account_id = account_id
        self._owner = owner
        self._balance = balance
        self._created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- Encapsulation using properties ---
    @property
    def account_id(self):
        return self._account_id

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, name):
        if not name.strip():
            raise ValueError("Owner name cannot be empty")
        self._owner = name

    @property
    def balance(self):
        return self._balance

    @property
    def created_at(self):
        return self._created_at

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        """Subclasses will define their own withdrawal behavior."""
        pass

    def to_dict(self):
        return {
            "id": self._account_id,
            "owner": self._owner,
            "balance": self._balance,
            "created_at": self._created_at,
            "type": self.__class__.__name__,
        }


# -----------------------
# Subclasses: Inheritance + Polymorphism
# -----------------------
class SavingsAccount(Account):
    """No overdraft allowed"""

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds in Savings Account")
        self._balance -= amount


class CheckingAccount(Account):
    """Can allow overdraft up to a limit"""

    def __init__(self, account_id: str, owner: str, balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(account_id, owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance + self._overdraft_limit:
            raise ValueError("Insufficient funds: Overdraft limit exceeded")
        self._balance -= amount

    def to_dict(self):
        d = super().to_dict()
        d["overdraft_limit"] = self._overdraft_limit
        return d


# -----------------------
# Bank class (Manager)
# -----------------------
class Bank:
    """Manages all accounts and performs CRUD + business logic"""

    DATA_FILE = "bank_data.json"

    def __init__(self):
        self.accounts = {}
        self.transactions = []
        self.load_data()

    # --- Persistence in JSON file (optional) ---
    def save_data(self):
        data = {
            "accounts": {aid: acc.to_dict() for aid, acc in self.accounts.items()},
            "transactions": self.transactions,
        }
        with open(self.DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.DATA_FILE):
            return
        with open(self.DATA_FILE, "r") as f:
            data = json.load(f)
            for aid, info in data.get("accounts", {}).items():
                if info["type"] == "SavingsAccount":
                    acc = SavingsAccount(aid, info["owner"], info["balance"])
                else:
                    acc = CheckingAccount(aid, info["owner"], info["balance"], info.get("overdraft_limit", 0))
                self.accounts[aid] = acc
            self.transactions = data.get("transactions", [])

    # --- CRUD Operations ---
    def create_account(self, acc_type: str, owner: str, initial_deposit: float, overdraft_limit: float = 0.0):
        acc_id = str(uuid.uuid4())[:8]
        if acc_type.lower() == "savings":
            acc = SavingsAccount(acc_id, owner, initial_deposit)
        else:
            acc = CheckingAccount(acc_id, owner, initial_deposit, overdraft_limit)
        self.accounts[acc_id] = acc
        self._log_transaction(acc_id, "CREATE", initial_deposit, f"New {acc_type} account created")
        self.save_data()
        return acc

    def get_account(self, acc_id: str):
        return self.accounts.get(acc_id)

    def update_account_owner(self, acc_id: str, new_owner: str):
        acc = self.get_account(acc_id)
        if not acc:
            raise ValueError("Account not found")
        acc.owner = new_owner
        self._log_transaction(acc_id, "UPDATE", 0, f"Owner updated to {new_owner}")
        self.save_data()

    def delete_account(self, acc_id: str):
        acc = self.get_account(acc_id)
        if not acc:
            raise ValueError("Account not found")
        if acc.balance != 0:
            raise ValueError("Account balance must be zero to delete")
        del self.accounts[acc_id]
        self._log_transaction(acc_id, "DELETE", 0, "Account deleted")
        self.save_data()

    def list_accounts(self):
        return [acc.to_dict() for acc in self.accounts.values()]

    # --- Banking Operations ---
    def deposit(self, acc_id: str, amount: float):
        acc = self.get_account(acc_id)
        if not acc:
            raise ValueError("Account not found")
        acc.deposit(amount)
        self._log_transaction(acc_id, "DEPOSIT", amount, "Amount deposited")
        self.save_data()

    def withdraw(self, acc_id: str, amount: float):
        acc = self.get_account(acc_id)
        if not acc:
            raise ValueError("Account not found")
        acc.withdraw(amount)
        self._log_transaction(acc_id, "WITHDRAW", amount, "Amount withdrawn")
        self.save_data()

    def transfer(self, from_id: str, to_id: str, amount: float):
        src = self.get_account(from_id)
        dest = self.get_account(to_id)
        if not src or not dest:
            raise ValueError("One or both accounts not found")
        src.withdraw(amount)
        dest.deposit(amount)
        self._log_transaction(from_id, "TRANSFER_OUT", amount, f"To {to_id}")
        self._log_transaction(to_id, "TRANSFER_IN", amount, f"From {from_id}")
        self.save_data()

    # --- Transaction Log ---
    def _log_transaction(self, acc_id, tx_type, amount, desc):
        self.transactions.append({
            "id": str(uuid.uuid4())[:8],
            "account_id": acc_id,
            "type": tx_type,
            "amount": amount,
            "description": desc,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })

    def list_transactions(self, acc_id=None):
        if not acc_id:
            return self.transactions[-10:]  # show last 10 by default
        return [t for t in self.transactions if t["account_id"] == acc_id]


# -----------------------
# CLI Menu
# -----------------------
def show_menu():
    print("\n==== BANKING SYSTEM ====")
    print("1. Create account")
    print("2. View account")
    print("3. Update owner")
    print("4. Delete account")
    print("5. List all accounts")
    print("6. Deposit")
    print("7. Withdraw")
    print("8. Transfer")
    print("9. View transactions")
    print("0. Exit")


def main():
    bank = Bank()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                owner = input("Enter owner name: ")
                acc_type = input("Type (savings/checking): ").lower()
                deposit = float(input("Initial deposit: "))
                od = 0
                if acc_type == "checking":
                    od = float(input("Overdraft limit (0 if none): "))
                acc = bank.create_account(acc_type, owner, deposit, od)
                print(f"Account created! ID: {acc.account_id}")
            elif choice == "2":
                aid = input("Enter Account ID: ")
                acc = bank.get_account(aid)
                if acc:
                    print(acc.to_dict())
                else:
                    print("Account not found.")
            elif choice == "3":
                aid = input("Account ID: ")
                new_owner = input("New owner name: ")
                bank.update_account_owner(aid, new_owner)
                print("Owner updated.")
            elif choice == "4":
                aid = input("Account ID: ")
                bank.delete_account(aid)
                print("Account deleted.")
            elif choice == "5":
                for a in bank.list_accounts():
                    print(a)
            elif choice == "6":
                aid = input("Account ID: ")
                amt = float(input("Deposit amount: "))
                bank.deposit(aid, amt)
                print("Deposit successful.")
            elif choice == "7":
                aid = input("Account ID: ")
                amt = float(input("Withdraw amount: "))
                bank.withdraw(aid, amt)
                print("Withdrawal successful.")
            elif choice == "8":
                from_id = input("From Account ID: ")
                to_id = input("To Account ID: ")
                amt = float(input("Amount to transfer: "))
                bank.transfer(from_id, to_id, amt)
                print("Transfer successful.")
            elif choice == "9":
                aid = input("Account ID (leave blank for all): ")
                txs = bank.list_transactions(aid or None)
                for t in txs:
                    print(t)
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()