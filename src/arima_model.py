import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima(series, order=(5,1,0)):
    model = ARIMA(series, order=order)
    return model.fit()
