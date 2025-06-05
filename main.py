from expense import Expense
from storage import store_expense, load_expense
from report import summarize_by_category


df = load_expense("expenses.csv")
summary = summarize_by_category(df)
print(summary)