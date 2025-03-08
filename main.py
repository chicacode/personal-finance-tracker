# Imports
from visualization import plot_spending_by_category
from menu import main_menu
from budget_management import (
    set_budget,
    add_transaction,
    get_user_transaction,
    calculate_spending,
    top_spending_categories
)

from data_management import (
    load_data, view_data, date_range, add_tran, edit_tran, delete_transaction
)
from data_analyze import (
analyze_spending, average_monthly_spending, save_to_csv
)
# CSV
file_path = "sampledata.csv"

load_data(file_path)

# 1️⃣ Set a Monthly Budget
BUDGET = 4000

data = load_data(file_path)
print(data)

def main():
    data = load_data(file_path)
    while True:
        # Choice verification
        main_menu()
        user_choice = input("Your Choice : ")
        if user_choice in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']:

            # Main choices
            if user_choice == '0':
                data = load_data(file_path)
                print("\033[32mCSV file imported successfully.\033[0m")
            elif user_choice == '1':
                view_data(data)
            elif user_choice == '2':
                date_range(data)
            elif user_choice == '3':
                print("\nAdd a new transaction")
                if data is not None:
                    data.to_csv(file_path, index=False)

                    add_tran(data)
                    date, category, description, amount, typetrans = get_user_transaction()

                    # Update data with new transaction
                    data = add_transaction(data, date, category, description, amount, typetrans)
                else:
                    print("Error: Transaction could not be added.")
            elif user_choice == '4':
                # Update transaction
                edit_tran(data)
            elif user_choice == '5':
                # Delete transaction
                delete_transaction(data)
            elif user_choice == '6':
                # ✅ Calculate total spending and remaining budget
                # Analyze Spending by Category
                remaining_budget, total_spent = calculate_spending()
                print(f"\n💰 Total Spent: ${total_spent:.2f}")
                print(f"🟢 Remaining Budget: ${remaining_budget:.2f}")
            elif user_choice == '7':
               # Calculate Average Monthly Spending
                if data is not None and not data.empty:
                    average_monthly_spending(data)
                else:
                    print("No transactions found.")
            elif user_choice == '8':
                # ✅ Display Top Spending Categories
                top_categories = top_spending_categories()
                print("\n🔥 Top Spending Categories:")
                for cat, amount in top_categories.items():
                    print(f"- {cat}: ${amount:.2f}")
            elif user_choice == '9':
                # ✅ Visualize spending
                plot_spending_by_category(data)
            elif user_choice == '10':
                # Set Budget
                set_budget(BUDGET)
            elif user_choice == '11':
                # Save transaction
                date, category, description, amount, typetrans = get_user_transaction()

                # Update data with new transaction
                data = add_transaction(data, date, category, description, amount, typetrans)
            elif user_choice == '12':
                print("Exiting the Personal Finance Tracker. Goodbye!")
                break  # Exit the program

        else:
            print("\033[31mInvalid choice! Please, try again.\033[0m")


if __name__ == "__main__":
    main()


