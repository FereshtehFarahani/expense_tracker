import unittest
from expense import Expense
import datetime

class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense("01-06-2025", "Food", "Lunch", 12.50)
        self.assertEqual(expense.date, datetime.datetime(2025, 6, 1))
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Lunch")
        self.assertEqual(expense.amount, 12.50)

    def test_to_dict(self):
        expense = Expense("01-06-2025", "Transport", "Bus ticket", 3.00)
        result = expense.to_dict()
        expected = {
            "date": datetime.datetime(2025, 6, 1),
            "category": "Transport",
            "description": "Bus ticket",
            "amount": 3.00
        }
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
