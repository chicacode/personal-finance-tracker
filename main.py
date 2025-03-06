from visualization import plot_spending_by_category
from budget_management import set_budget, add_transaction, get_user_transaction
import pandas as pd

file_path = "sampledata.csv"


def load_data(file):
    """Load transactions from a CSV file, or create an empty DataFrame if missing."""
    try:
        return pd.read_csv(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount", "Type"])

    # 1️⃣ Set a Monthly Budget
    set_budget(4000)


    print(data)

    # 2️⃣ Add Transactions
    for date, category, description, amount, type in [
        ("2025-02-27", "Entertainment", "Movie", 15.00, "Entertainment"),
        ("2025-03-05", "Food", "Lunch", 32.50, "Restaurant"),
        ("2025-03-06", "Transport", "Compass Ticket", 105.00,  "Expense")
    ]:
        data = add_transaction(date, category, description, amount, type)

    # Save initial transactions
    data.to_csv(file_path, index=False)

def main():
    data = load_data(file_path)
    while True:
        print("\nAdd a new transaction")
        date, category, description, amount, type = get_user_transaction()
        data = add_transaction(data, date, category, description, amount, type)
        if data is not None:
            data.to_csv(file_path, index=False)
            print("Transaction added successfully!")
            # Show updated spending chart
            plot_spending_by_category(data)
        else:
            print("Error: Transaction could not be added.")

        next_transaction = input("Do you want to add another transaction? (yes/no): ").strip().lower()
        if next_transaction != 'yes':
            break


if __name__ == "__main__":
    main()


