from visualization import plot_spending_by_category
from budget_management import set_budget
import pandas as pd

file_path = "sampledata.csv"

def load_data(file_path):
    """Load transactions from a CSV file."""
    return pd.read_csv(file_path)

data = load_data(file_path)

print(data)

# 1️⃣ Set a Monthly Budget
set_budget(4000)

plot_spending_by_category(data)