import pandas as pd

def preprocess_data(filepath):
    data = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    return data
