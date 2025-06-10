from expense import Expense
from storage import store_expense, load_expense
from report import summarize_by_category,summarize_monthly_yearly, plot_expenses


def add_expense():
    answer = input("Do you want to enter new expense? (yes/no)").strip().lower() #normalizing the answer
    if answer == 'yes':
        try:
            values = input("Values: date,category,description,amount ").split()
            if len(values) != 4:
                raise ValueError("Expected 4 values")
            date,category,description,amount = values
            amount = float(amount)
            expense = Expense(date, category, description, amount)
            store_expense(expense)
            print("✅ Expense saved!")
        except ValueError as e:
                print("❌ Invalid input. Example: 01-06-2025 Food Lunch 12.5")


def view_summary():
    df = load_expense("expenses.csv")
    total_spent = df['amount'].sum()
    print(f"\n💸 Total spent: {total_spent:.2f}\n")

    print("📊 Expenses by Category:\n")
    print(summarize_by_category(df))

    print("\n🗓️ Monthly and Yearly Summary:\n")
    print(summarize_monthly_yearly(df))


def show_plot():
    df = load_expense("expenses.csv")
    plot_expenses(df)

def exit_app():
    print("app exiting")
    exit()

def show_menu():
    print("\nWhat do you want to do?")
    print("1. Add new expense")
    print("2. View monthly/yearly/category summary")
    print("3. Show expense plot")
    print("4. Exit")



if __name__ == "__main__":
    
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            df = load_expense("expenses.csv")
            show_plot()
        elif choice == '4':
            exit_app()
        else:
            print("❌ Invalid input. Please choose between 1-4.")




