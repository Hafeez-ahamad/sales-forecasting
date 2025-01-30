import matplotlib.pyplot as plt
import pandas as pd

def visualize_results(train, test, forecast):
    plt.figure(figsize=(10, 6))
    plt.plot(train.index, train['Sales'], label='Training Data')
    plt.plot(test.index, test['Sales'], label='Actual Sales')
    plt.plot(test.index, forecast, label='Forecasted Sales')
    plt.title('Sales Forecasting with ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.savefig('../results/forecast_results.png')
    plt.show()
