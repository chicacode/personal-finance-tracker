import pandas as pd
import matplotlib.pyplot as plt

class PersonalFinanceTracker:
    def __init__(self):
        """Initialize the finance tracker with an empty transactions DataFrame and budget dictionary."""
        self.transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        self.budgets = {}  # Stores budget limits for categories
        self.income = 0  # Stores total income

    def delete_transaction(self, index):
        """Delete a transaction by index."""
        if index < 0 or index >= len(self.transactions):
            print("Invalid index!")
            return

        self.transactions = self.transactions.drop(index).reset_index(drop=True)
        print("Transaction deleted successfully!")

    def analyze_spending(self):
        """Summarize total spending per category."""
        expenses = self.transactions[self.transactions['Type'] == 'Expense']
        category_totals = expenses.groupby('Category')['Amount'].sum()
        print("--- Total Spending by Category ---")
        print(category_totals)

    def average_monthly_spending(self):
        """Calculate and display the average monthly spending."""
        expenses = self.transactions[self.transactions['Type'] == 'Expense']
        expenses['Month'] = expenses['Date'].dt.to_period('M')
        avg_spending = expenses.groupby('Month')['Amount'].sum().mean()
        print(f"--- Average Monthly Spending: ${avg_spending:.2f} ---")

    def save_to_csv(self, filename):
        """Save transactions to a CSV file."""
        self.transactions.to_csv(filename, index=False)
        print(f"Transactions saved to {filename}")

    def menu(self):
        """Display a user-friendly menu for performing various finance tracking operations."""
        while True:
            print("\n=== Personal Finance Tracker ===")
            options = [
                "Import CSV File", "View Transactions", "Add Transaction", "Edit Transaction", "Delete Transaction",
                "Analyze Spending", "Average Monthly Spending", "Top Spending Category", "Visualize Spending",
                "Set Income", "Set Budget", "Check Budget Status", "Save Transactions to CSV", "Exit"
            ]
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")

            choice = input("Choose an option: ")
            if choice == '14': break
            try:
                getattr(self, options[int(choice) - 1].lower().replace(" ", "_"))()
            except:
                print("Invalid choice. Please try again.")


# Run the finance tracker menu
tracker = PersonalFinanceTracker()
tracker.menu()
