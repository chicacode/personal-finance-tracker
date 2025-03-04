# Personal Finance Tracker App

## Description

The **Personal Finance Tracker App** is an interactive, text-based Python application that helps users manage and analyze their personal spending habits. It allows users to import CSV transaction data, view, add, edit, and delete transactions, and analyze their spending patterns. The app also includes data visualization features to display monthly spending trends and the top spending categories. The project uses Python, `pandas` for data handling, and `matplotlib` for visualization. GitHub is used for collaboration and version control throughout the development process.

## Objective

The objective of this project is to build an interactive app that simulates personal finance management. It enables users to track and analyze their financial data and visualize trends through various charts.

## Technologies Used

- Python
- pandas (for data handling and manipulation)
- matplotlib (for data visualization)
- GitHub (for collaboration and version control)

## Features

### 1. File Import Functionality
- Import CSV files containing transaction data (e.g., `sampledata.csv`) with fields: `date`, `category`, `description`, and `amount`.
- Error handling for incorrect file formats or missing columns.

### 2. Data Management
- **View Transactions by Date Range**: Filter and display transactions within a specified date range.
- **Add a Transaction**: Add new transactions with details like date, category, description, and amount.
- **Edit a Transaction**: Modify the details of an existing transaction (date, category, description, amount).
- **Delete a Transaction**: Remove a transaction by its index.

### 3. Spending Analysis
- **Analyze Spending by Category**: Display total spending for each category.
- **Calculate Average Monthly Spending**: Calculate the average spending per month.
- **Show Top Spending Category**: Identify the category with the highest total spending.

### 4. Data Visualization
- **Monthly Spending Trend**: Visualize spending trends over time using a line chart.
- **Spending by Category**: Generate a bar chart showing total spending by category.
- **Percentage Distribution**: Display a pie chart representing the distribution of spending across categories.

### 5. Save Transactions to CSV
- Save the updated transaction list to a CSV file for record-keeping.

### 6. User Interaction
- A text-based interface with a menu-driven system for easy navigation through the app's features.

### 7. GitHub Collaboration
- Team members collaborate using GitHub by:
  - Creating branches for different modules (e.g., data management, analysis, and visualization).
  - Using pull requests for merging work after review.
  - Documenting the project setup and usage in this `README.md`.

## Modules

- **Data Management Module**: Handles file import, viewing, adding, editing, and deleting transactions.
- **Data Analysis Module**: Includes functions to analyze spending by category, calculate average monthly spending, and identify the top spending category.
- **Visualization Module**: Uses `matplotlib` to generate line, bar, and pie charts to visualize spending trends and distributions.

## Workflow and Requirements

### Technologies:
- Python
- pandas
- matplotlib
- GitHub

### Dataset:
- A CSV file with columns: `Date`, `Category`, `Description`, and `Amount`. You can use a sample CSV or import your own transaction file.

### Deliverables:
- Complete code on GitHub with clear, documented commits.
- A structured README file.
- A presentation demonstrating the app’s functionality, insights, and visualizations.

## Sample Menu

When the app starts, it presents the following menu:

=== Personal Finance Tracker === 0. Import a CSV File

1. View All Transactions
2. View Transactions by Date Range
3. Add a Transaction
4. Edit a Transaction
5. Delete a Transaction
6. Analyze Spending by Category
7. Calculate Average Monthly Spending
8. Show Top Spending Category
9. Visualize Monthly Spending Trend
10. Save Transactions to CSV
11. Exit Choose an option (1-11):