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
    df.plot(x='date', y='amount',kind = 'hist', title='Expenses Over Time')
    df.plot(x='category', y='amount', kind = 'hist', title='Expenses Over Time')
    return plt.show()