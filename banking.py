"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    if account_number in accounts:
        return f"Account number {account_number} already exists"
    else:

    
        accounts[account_number] = {
        "account_number": account_number,
        "name": name,
        **kwargs  
         }
    return f"Account for {name} with account number {account_number} created successfully"

print(create_account(1001, "Alice", balance=500.0, account_type="savings"))
print(create_account(1002, "Alice", balance=700.0, account_type="savings"))
print(accounts)

"""Create an account with optional features like overdraft_limit."""
  

def deposit(account_number, amount):
    if account_number not in accounts:
        return f"{account_number} does not exist"
    else:
        if "balance" not in accounts[account_number]:
            accounts[account_number]["balance"] = 0
        accounts[account_number]["balance"] += amount
        name = accounts[account_number]["name"]
    return f"Deposited {amount} into {name}'s account"
print(deposit(1001,10000))   
print(accounts)       
"""Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
"""
    

def withdraw(account_number, amount):
    if account_number not in accounts:
        return f"Account number {account_number} does not exist"
    if "balance" not in accounts[account_number]:
        return f"Account {account_number} has no balance"
    if amount <= 0:
        return f"Withdrawal amount must be positive"
    if amount > accounts[account_number]["balance"]:
        return f"Insufficient funds"
    else:
        accounts[account_number]["balance"] -= amount
        name = accounts[account_number]["name"]
        return f"Withdrawn {amount} successfully from {name}'s account, new balance: {accounts[account_number]['balance']}" 
print(withdraw(1001,2000))

"""Withdraw money if balance is sufficient. else: insufficient funds"""
    

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts if funds are sufficient."""
    if from_acc not in accounts:
        return f"Source account {from_acc} does not exist"
    if to_acc not in accounts:
        return f"Destination account {to_acc} does not exist"
    
    if "balance" not in accounts[from_acc]:
        return f"Source account {from_acc} has no balance"
    
    
    if amount <= 0:
        return f"Transfer amount must be positive"
    
    
    if amount > accounts[from_acc]["balance"]:
        return f"Insufficient funds in account {from_acc}"
    
    
    if "balance" not in accounts[to_acc]:
        accounts[to_acc]["balance"] = 0

    accounts[from_acc]["balance"] -= amount
    accounts[to_acc]["balance"] += amount
    
    from_name = accounts[from_acc]["name"]
    to_name = accounts[to_acc]["name"]
    return f"Transferred {amount} from {from_name}'s account ({from_acc}) to {to_name}'s account ({to_acc})"

print(transfer(1001,1002,2000))
print(accounts)
