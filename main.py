from expense import Expense
from storage import store_expense, load_expense
from report import summarize_by_category,summarize_monthly_yearly, plot_expenses
import pandas as pd
import matplotlib.pyplot as plt


def add_expense():
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


def view_summary(df):
    total_spent = df['amount'].sum()
    print(f"\n💸 Total spent: {total_spent:.2f}\n")

    print("📊 Expenses by Category:\n")
    print(summarize_by_category(df))

    print("\n🗓️ Monthly and Yearly Summary:\n")
    print(summarize_monthly_yearly(df))


def show_plot(df):
    plot_expenses(df)

def exit_app():
    print("app exiting")
    exit()



if __name__ == "__main__":

    while True:
        print("\nWhat do you want to do?")
        print("1. Add new expense")
        print("2. View monthly/yearly/category summary")
        print("3. Show expense plot")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            df = load_expense("expenses.csv")
            view_summary(df)
        elif choice == '3':
            df = load_expense("expenses.csv")
            show_plot(df)
        elif choice == '4':
            exit_app()
        else:
            print("Invalid input. Please choose between 1-4.")




