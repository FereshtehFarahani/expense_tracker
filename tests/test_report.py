import unittest
import pandas as pd
from report import summarize_by_category, summarize_monthly_yearly, plot_expenses

class TestReport(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.df = pd.DataFrame([
            {"date": "2025-06-01", "category": "Food", "description": "Lunch", "amount": 10.0},
            {"date": "2025-06-01", "category": "Transport", "description": "Taxi", "amount": 20.0},
            {"date": "2025-06-15", "category": "Food", "description": "Dinner", "amount": 30.0},
            {"date": "2025-07-01", "category": "Food", "description": "Snack", "amount": 5.0},
            {"date": "2024-12-01", "category": "Transport", "description": "Bus", "amount": 3.0},
        ])
        self.df['date'] = pd.to_datetime(self.df['date'])  # Convert 'date' column to datetime

    def test_summarize_by_category(self):
        result = summarize_by_category(self.df)
        expected = pd.DataFrame({
            'category': ['Food', 'Transport'],
            'amount': [45.0, 23.0]
        })
        pd.testing.assert_frame_equal(result.sort_values('category').reset_index(drop=True),
                                      expected.sort_values('category').reset_index(drop=True))

    def test_summarize_monthly_yearly(self):
        result = summarize_monthly_yearly(self.df)
        expected = pd.DataFrame({
            'year': [2024, 2025, 2025],
            'month': [12, 6, 7],
            'amount': [3.0, 60.0, 5.0]
        })
        pd.testing.assert_frame_equal(result.sort_values(['year', 'month']).reset_index(drop=True),
                                      expected.sort_values(['year', 'month']).reset_index(drop=True))

    def test_plot_expenses_runs(self):
        try:
            plot_expenses(self.df)
        except Exception as e:
            self.fail(f"plot_expenses() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
