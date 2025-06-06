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
    
    # enter new expense
    answer = input("Do you want to enter new expense? (yes/no)").strip().lower() #normalizing the answer
    if answer == 'yes':
        try:
            date,category,description,amount= input("Values: date,category,description,amount ").split()
            amount = float(amount)
            expense = Expense(date, category, description, amount)
            store_expense(expense)
            df = load_expense('expenses.csv')
            print(df)
        except ValueError as e:
                print("Please enter 4 values separated by spaces. Example: 01-06-2025 Food Lunch 12.5")
    else:
        print("app exiting")
        exit()

