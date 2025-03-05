from visualization import plot_spending_by_category
from budget_management import set_budget, add_transaction
import pandas as pd

file_path = "sampledata.csv"

def load_data(file_path):
    """Load transactions from a CSV file."""
    return pd.read_csv(file_path)

data = load_data(file_path)

print(data)

# 1️⃣ Set a Monthly Budget
set_budget(4000)

# 2️⃣ Add Transactions
add_transaction("2025-02-27", "Entertainment", "Movie", 15.00)
add_transaction("2025-03-05", "Food", "Lunch", 32.50)
add_transaction("2025-03-06", "Transport", "Compass Ticket", 105.00)


plot_spending_by_category(data)