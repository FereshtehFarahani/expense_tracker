import datetime
import csv 
import pandas as pd

class Expense:

  def __init__(self, date, category, description, amount):
    self.date = datetime.datetime.strptime(date, "%d-%m-%Y")
    self.category = category
    self.description = description
    self.amount = amount

  def to_dict(self):
    return {
    "date": self.date,
    "category": self.category,
    "description": self.description,
    "amount": self.amount
    }


e1 = Expense('05-06-2025', 'Food', 'Lunch at restaurant', 25.50)
#print(e1.to_dict())


def store_expense(expense):
    csv_file = 'expenses.csv'
    data = expense.to_dict()
    data['date'] = data['date'].strftime("%Y-%m-%d")  # convert datetime to string
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()  # Write header only if file is empty
        writer.writerow(data)        

store_expense(e1)

def load_expense(inputfile):
    expenses = []
    with open(inputfile, mode ='r') as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            row['date'] = datetime.datetime.strptime(row['date'], "%Y-%m-%d")
            row['category'] = row['category']
            row['description'] = row['description']
            row['amount'] = float(row['amount'])
            expenses.append(row) # add each row to the list 
    return pd.DataFrame(expenses)



df = load_expense('expenses.csv')
print("Total expenses:", df['amount'].sum())

