import unittest
import tempfile
import os
import pandas as pd
from expense import Expense
from storage import store_expense, load_expense

class TestStorage(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        self.test_file.close()  # Close so it can be used elsewhere
        self.expense = Expense("01-06-2025", "Food", "Lunch", 12.50)

    def tearDown(self):
        # Clean up the temporary file
        os.remove(self.test_file.name)

    def test_store_and_load_expense(self):
        # Store one expense
        store_expense(self.expense, filename=self.test_file.name)

        # Load it back
        df = load_expense(self.test_file.name)

        # Check if one row is loaded
        self.assertEqual(len(df), 1)

        # Check data matches
        row = df.iloc[0]
        self.assertEqual(row['category'], "Food")
        self.assertEqual(row['description'], "Lunch")
        self.assertEqual(row['amount'], 12.50)
        self.assertEqual(row['date'].date(), self.expense.date.date())

