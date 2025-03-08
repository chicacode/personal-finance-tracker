import matplotlib.pyplot as plt

def plot_spending_by_category(data):
    spending = data.groupby('Category')['Amount'].sum()
    spending.plot(kind='bar', title="Spending by Category", ylabel="Amount ($)")
    plt.show()
