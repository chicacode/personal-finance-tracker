import os.path
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

def add_transaction(df, date, category, description, amount, typetrans):
    """Add transaction to CSV File."""
    new_transaction = pd.DataFrame([[date, category, description, amount, typetrans]],
                                   columns=["Date", "Category", "Description", "Amount", "Type"])

    df = pd.concat([df, new_transaction], ignore_index=True)

    if os.path.exists(TRANSACTIONS_FILE):
        data = pd.read_csv(TRANSACTIONS_FILE)
        data = pd.concat([data, new_transaction], ignore_index=True)
    else:
        data = new_transaction

    # Save to CSV
    data.to_csv(TRANSACTIONS_FILE, index=False)
    print(f"Transaction added: {category} - ${amount}")

    return df

def load_transactions():
    """Load all transactions from the CSV file."""
    if os.path.exists(TRANSACTIONS_FILE):
        return pd.read_csv(TRANSACTIONS_FILE)
    return pd.DataFrame(columns=["Date", "Category", "Description", "Amount", "Type"])

def get_user_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    typetrans = input("Enter the transaction type: ")
    return date, category, description, amount, typetrans

# Analyzing Spending
def calculate_spending():
    """Calculate total spending and remaining budget."""
    budget = load_budget()
    transactions = load_transactions()

    if transactions.empty:
        return budget, 0

    total_spent = transactions["Amount"].sum()
    remaining_budget = budget - total_spent
    return remaining_budget, total_spent

def top_spending_categories(n=3):
    """Find the top N spending categories."""
    transactions = load_transactions()
    if transactions.empty:
        return {}

    category_spending = transactions.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    return category_spending.head(n).to_dict()