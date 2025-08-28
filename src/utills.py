import matplotlib.pyplot as plt

def plot_forecasts(actual, arima_pred, lstm_pred):
    plt.figure(figsize=(10,6))
    plt.plot(actual.index, actual, label="Actual")
    plt.plot(actual.index, arima_pred, label="ARIMA Forecast")
    plt.plot(actual.index, lstm_pred, label="LSTM Forecast")
    plt.legend()
    plt.show()
