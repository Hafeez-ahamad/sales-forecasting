import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib

def train_model(data):
    train = data.iloc[:-12]  # Use all but the last 12 months for training
    model = ARIMA(train['Sales'], order=(5, 1, 0))  # Example order (p, d, q)
    model_fit = model.fit()

    # Save model
    joblib.dump(model_fit, '../models/arima_model.pkl')
    return model_fit
