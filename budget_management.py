import pandas as pd

BUDGET_FILE = "budget.csv"
TRANSACTIONS_FILE = "sampledata.csv"

def set_budget(amount):
    """Set a monthly budget"""
    data = pd.DataFrame({"Budget" : [amount]})
    data.to_csv(BUDGET_FILE, index=False)
    print(f"✅ Budget set to ${amount}")