from expense import Expense
from storage import store_expense, load_expense
from report import summarize_by_category,summarize_monthly_yearly, plot_expenses
import datetime


VALID_CATEGORIES = {"Food", "Transport", "Entertainment", "Utilities", "Other"}  


def add_expense():
    answer = input("Do you want to enter new expense? (yes/no)").strip().lower() #normalizing the answer
    if answer == 'yes':
        try:
            date_str, category, description, amount_str = input(
                "Values: date (YYYY-MM-DD), category, description, amount: "
            ).split()

            # Validate date
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                print("❌ Invalid date format. Please use YYYY-MM-DD.")
                return

            # Validate amount
            try:
                amount = float(amount_str)
                if amount <= 0:
                    print("❌ Amount must be a positive number.")
                    return
            except ValueError:
                print("❌ Amount must be a valid number.")
                return

            # Validate category (case-insensitive match)
            matched_category = None
            for valid in VALID_CATEGORIES:
                if category.lower() == valid.lower():
                    matched_category = valid  # use the original formatting
                    break
            if matched_category is None:
                print(f"❌ Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
                return
            category = matched_category

            # All good — store it
            expense = Expense(date_str, category, description, amount_str)
            store_expense(expense)
            print("✅ Expense saved!")

        except ValueError as e:
                print("❌ Please enter 4 values separated by spaces. Example: 2025-06-01 Food Lunch 12.5")
    else: 
        print("Exiting app.")


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




