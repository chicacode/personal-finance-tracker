from visualization import plot_spending_by_category
from budget_management import set_budget, add_transaction, get_user_transaction
import pandas as pd
import os.path

file_path = "sampledata.csv"

def load_data(file_path):
    """Load transactions from a CSV file."""
    if not os.path.exists(file_path):
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    return pd.read_csv(file_path)


# 2️⃣ Add Transactions
add_transaction("2025-02-27", "Entertainment", "Movie", 15.00)
add_transaction("2025-03-05", "Food", "Lunch", 32.50)
add_transaction("2025-03-06", "Transport", "Compass Ticket", 105.00)

def main():
    # 1️⃣ Set a Monthly Budget
    set_budget(4000)
    
    data = load_data(file_path)
    while True:
        print("\nAdd a new transaction")
        date, category, description, amount = get_user_transaction()
        data = add_transaction(date, category, description, amount)
        data.to_csv(file_path, index=False)
        print("Transaction added successfully!")
        plot_spending_by_category(data)

        cont = input("Do you want to add another transaction? (yes/no): ").strip().lower()
        if cont != 'yes':
            break


if __name__ == "__main__":
    main()


