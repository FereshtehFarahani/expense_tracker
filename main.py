from expense import Expense
from storage import store_expense, load_expense
from report import summarize_by_category,summarize_monthly_yearly, plot_expenses
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = load_expense("expenses.csv")

    total_spent = df['amount'].sum()
    print(f"\n💸 Total spent: {total_spent:.2f}\n")

    print("📊 Expenses by Category:\n")
    print(summarize_by_category(df))

    print("\n🗓️ Monthly and Yearly Summary:\n")
    print(summarize_monthly_yearly(df))

    plot_expenses(df)
