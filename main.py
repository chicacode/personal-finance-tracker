from visualization import plot_spending_by_category
import pandas as pd

file_path = "sampledata.csv"

def load_data(file_path):
    """Load transactions from a CSV file."""
    return pd.read_csv(file_path)

data = load_data(file_path)

print(data)

plot_spending_by_category(data)