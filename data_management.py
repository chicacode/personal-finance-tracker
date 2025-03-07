import pandas as pd
import datetime

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
data = load_data(file_path)

#  Add a Transaction
def date_range(data):
    """Filter date range"""

    while True:
        start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
        end_date = input("Enter the end date (YYYY-MM-DD): ").strip()
        try:
            if end_date < start_date:
                print("\033[31mEnd date can't be earlier than start date. Please try again.\033[0m")
                continue

            if len(start_date) != 10:
                print("\033[31mInvalid deadline. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
                continue
            if len(end_date) != 10:
                print("\033[31mInvalid deadline. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
                continue

            filter_date = (data["Date"] >= start_date) & (data["Date"] <= end_date)
            filter_final_date = data[filter_date]

            if filter_final_date.empty:
                print(f"\033[31mNo transactions found between {start_date} and {end_date}.\033[0m")
                continue

            else:
                print()
                print(f"--- Transactions from {start_date} to {end_date} ---")
                print(filter_final_date)

            break

        except Exception as e:
            print(f"\033[31mNo transactions found between {start_date} and {end_date}.\033[0m")
            continue

# 3️⃣ Add a Transaction
def add_tran(data):
    """Add the transaction"""
    # Date
    while True:
        date = input("Enter the date (YYYY-MM-DD) : ").strip()
        try:
            enter_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            today = datetime.date.today()
            if enter_date < today:
                print("\033[31mThe date can't be past date.\033[0m")
                continue
            if len(date) != 10:
                print("\033[31mInvalid date. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
                continue
            else:
                break

        except ValueError:
            print("\033[31mInvalid date. Please enter in YYYY-MM-DD format.(Ex. 2025-05-31)\033[0m")
            continue

    # Category
    while True:
        category = input("Enter the category (e.g., Food, Rent): ").strip()
        if not category:
            print("\033[31mCategory can't be empty. Please try again.\033[0m")
            continue
        else:
            break

    # Description:
    while True:
        description = input("Enter the description : ")
        if not description:
            print("\033[31mDescription can't be empty. Please try again.\033[0m")
            continue
        else:
            break

    # Amount
    while True:
        amount = input("Enter the amount : ")
        if not amount:
            print("\033[31mAmount can't be empty. Please try again.\033[0m")
            continue
        else:
            break

    # Type
    while True:
        type = input("Enter the type (1 = Expense, 2 = Income) : ").strip()
        if type not in ["1", "2"]:
            print("\033[31mInvalid type. Please enter 1 or 2\033[0m")
            continue
        else:
            break

    new_row = pd.DataFrame([{
        "Date" : date,
        "Category" : category,
        "Description" : description,
        "Amount" : amount,
        "Type" : type
    }])

    data = pd.concat([data, new_row], ignore_index = True)

    print("\033[32mTransaction added successfully!\033[0m")
    return data

# 4️⃣ Edit a Transaction
def edit_tran(data):
    """Edit the transaction"""
    #choice view or edit
    while True:
        choice = input("Do you want to view all transactions first? (y/n):").strip()
        if choice == "y" or choice == "Y":
            view_data(data)
            break
        if choice == "n" or choice == "N":
            break
        else:
            print("\033[31mInvalid input. Please enter y or n.\033[0m")
    #choice index
    while True:
        try:
            enter = int(input("Enter the index of the transaction to edit : "))
            if enter < 0 or enter > len(data):
                print("\033[31mInvalid index. Please enter again.\033[0m")
                continue
            break
        except ValueError:
            print("\033[31mInvalid input. Please enter a number.\033[0m")
    #view transaction
    transaction = data.iloc[enter]
    print("Current Transaction Details:")
    print(transaction)
    #edit transaction
    new_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ").strip() or transaction["Date"]
    new_category = input("Enter new category or press Enter to keep current: ").strip() or transaction["Category"]
    new_description = input("Enter new description or press Enter to keep current: ").strip() or transaction["Description"]
    new_amount = input("Enter new amount or press Enter to keep current: ").strip() or transaction["Amount"]

    #edit transaction_type
    while True:
        new_type = input("Enter new type (1 = Expense, 2 = Income) or press Enter to keep current: ").strip() or transaction["Type"]
        if new_type == '1':
            new_type = "Expense"
            break
        elif new_type == '2':
            new_type = "Income"
            break
        elif new_type == "":
            new_type = transaction["Type"]
            break
        else:
            print("\033[31mInvalid type. Please enter 1 for Expense or 2 for Income.\033[0m")

    #renew transaction
    data.at[enter, 'Date'] = new_date
    data.at[enter, 'Category'] = new_category
    data.at[enter, 'Description'] = new_description
    data.at[enter, 'Amount'] = float(new_amount)
    data.at[enter, 'Type'] = new_type

    print("\033[32mTransaction updated successfully!\033[0m")