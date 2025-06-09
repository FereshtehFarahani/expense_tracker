# Expense_tracker 

## app structure 
<pre lang="markdown">
expense_tracker/
├── expense.py
├── storage.py
├── report.py
├── main.py
├── expenses.csv
├── README.md
└── requirements.txt
├── tests/
│   └── test_expense.py
│   └── test_storage.py
│   └── test_report.py
</pre>

## plots
![expenses_by_category](expenses_by_category.png)
![expenses_over_time](expenses_over_time.png)


CLI Menu: 
<pre lang="markdown">
What do you want to do?
1. Add new expense
2. View monthly/yearly/category summary
3. Show expense plot
4. Exit
</pre>

Run tests 
<pre lang="markdown">
python -m unittest discover -s tests
</pre>