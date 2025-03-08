import pandas as pd

file_path = "sampledata.csv"

def load_data(file):
    """Load transactions from a CSV file, or create an empty DataFrame if missing."""
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount", "Type"])

# 1️⃣ View All Transactions
def view_data(data):
    """View all data"""
    print("--- All Transactions ---")
    print(data)
    print()

# 2️⃣ View Transactions by Date Range


def analyze_spending(data):
    """Summarize total spending per category."""
    if 'Type' not in data.columns or 'Category' not in data.columns:
        print("Error: Missing required columns in the dataset.")
        return

    expenses = data[data['Type'] == 'Expense'].copy()

    if expenses.empty:
        print("No expenses recorded yet.")
        return

    # ✅ Group by category and sum the amounts
    category_totals = expenses.groupby('Category')['Amount'].sum()

    print("\n--- Total Spending by Category ---")
    print(category_totals.to_string())


def average_monthly_spending(data):
    """Calculate and display the average monthly spending."""
    if data.empty:
        print("No transactions available to analyze.")
        return

    # Ensure the Date column is in datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Filter only 'Expense' transactions
    expenses = data.loc[data['Type'] == 'Expense'].copy()  # Copy to avoid SettingWithCopyWarning

    if expenses.empty:
        print("No expense transactions found.")
        return

    # Extract month and calculate average spending
    expenses['Month'] = expenses['Date'].dt.to_period('M')
    avg_spending = expenses.groupby('Month')['Amount'].sum().mean()

    print(f"--- Average Monthly Spending: ${avg_spending:.2f} ---")


def save_to_csv(data, filename):
    """Save transactions to a CSV file."""
    data.transactions.to_csv(filename, index=False)
    print(f"Transactions saved to {filename}")


