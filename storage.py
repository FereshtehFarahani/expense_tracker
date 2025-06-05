import datetime
import csv 
import pandas as pd


def store_expense(expense):
    csv_file = 'expenses.csv'
    data = expense.to_dict()
    data['date'] = data['date'].strftime("%Y-%m-%d")  # convert datetime to string
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:  # Check if file is empty
            writer.writeheader()  # Write header only if file is empty
        writer.writerow(data)        


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
