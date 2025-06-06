import pandas as pd
import matplotlib.pyplot as plt



def summarize_by_category(df):
    return df.groupby('category')['amount'].sum().reset_index()


def summarize_monthly_yearly(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    return df.groupby(['year','month'])['amount'].sum().reset_index()

def plot_expenses(df):
    # Plot expenses over time
    df = df.sort_values(by='date')
    df.plot(x='date', y='amount', kind='line', title='Expenses Over Time')
    plt.tight_layout()
    plt.savefig("expenses_over_time.png")  # Save plot to file
    plt.show()

    # Plot total expenses by category
    df.groupby('category')['amount'].sum().plot(kind='bar', title='Expenses by Category')
    plt.tight_layout()
    plt.savefig("expenses_by_category.png")
    plt.show()
  