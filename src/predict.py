import joblib
import pandas as pd

def predict_sales(model_path, steps=12):
    model = joblib.load(model_path)
    forecast = model.forecast(steps=steps)
    return forecast
