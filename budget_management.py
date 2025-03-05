import os.path

import pandas as pd

BUDGET_FILE = "budget.csv"
TRANSACTIONS_FILE = "sampledata.csv"

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