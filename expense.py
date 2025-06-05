import datetime


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


