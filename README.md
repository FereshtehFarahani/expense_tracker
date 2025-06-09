# Expense_tracker 

## app structure 
<pre lang="markdown">
expense_tracker/
│
├── expense.py        # The Expense class
├── storage.py        # store_expense() and load_expense()
├── report.py        # summarize and visualize
├── main.py          # main script that runs the app
└── expenses.csv      # expense data
</pre>

## plots
![expenses_by_category](expenses_by_category.png)
![expenses_over_time](expenses_over_time.png)


CLI menu: 
<pre lang="markdown">>
What do you want to do?
1. Add new expense
2. View monthly/yearly/category summary
3. Show expense plot
4. Exit
</pre>