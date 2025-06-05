import pandas as pd
import matplotlib.pyplot as plt

def summarize_by_category(df):
    return df.groupby('category')['amount'].sum().reset_index()