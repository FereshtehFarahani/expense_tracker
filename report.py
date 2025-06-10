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

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # Create a figure with 2 subplots: one for time series, one for category
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))

    # ---- Plot 1: Expenses Over Time (Line Plot) ----
    axes[0].plot(df['date'], df['amount'], marker='o', linestyle='-', color='tab:blue')
    axes[0].set_title("Expenses Over Time")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Amount (€)")
    axes[0].grid(True)

    # ---- Plot 2: Total Expenses by Category (Bar Plot) ----
    category_summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    category_summary.plot(kind='bar', ax=axes[1], color='tab:green')
    axes[1].set_title("Total Expenses by Category")
    axes[1].set_xlabel("Category")
    axes[1].set_ylabel("Total Amount (€)")
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].grid(axis='y')

    # Layout adjustments and save
    plt.tight_layout()
    plt.savefig("expense_summary.png")
    plt.show()
