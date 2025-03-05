import os.path
from unicodedata import category

import pandas as pd

BUDGET_FILE = "budget.csv"
TRANSACTIONS_FILE = "sampledata.csv"

# Set a budget
def set_budget(amount):
    """Set a monthly budget"""
    data = pd.DataFrame({"Budget" : [amount]})
    data.to_csv(BUDGET_FILE, index=False)
    print(f"✅ Budget set to ${amount}")

def load_budget():
    """Load budget from CSV file or return default if is not set a new one"""
    if os.path.exists(BUDGET_FILE):
        data = pd.read_csv(BUDGET_FILE)
        return data.loc[0, "Budget"]
    # Default budget
    return 3000

# Tracking Expenses

def add_transaction(date, category, description, amount):
    """Add transaction to CSV File."""
    transaction = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount]
    })

    if os.path.exists(TRANSACTIONS_FILE):
        data = pd.read_csv(TRANSACTIONS_FILE)
        data = pd.concat([data, transaction], ignore_index=True)
    else:
        data = transaction

    data.to_csv(TRANSACTIONS_FILE, index=False)
    print(f"Transaction added: {category} - ${amount}")


def load_transaction():
    """Load all transactions from the CSV file."""
    