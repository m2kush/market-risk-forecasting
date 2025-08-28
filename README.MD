# 📈 Time Series Forecasting – NIFTY 50 (ARIMA + LSTM)

This project demonstrates **time series forecasting** on the NIFTY 50 index using both **ARIMA** (classical statistical model) and **LSTM** (deep learning model).  
It compares traditional and modern approaches to stock market prediction.

---

## 📊 Project Structure
time-series-forecasting/
│── data/ # Dataset (NIFTY 50 CSV file)
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Source code (ARIMA, LSTM, utilities)
│── results/ # Forecast plots and results
│── requirements.txt # Dependencies
│── README.md # Project description

---

## 🗂 Example Data (Head)

| Date       | Close    | High     | Low      | Open     | Volume |
|------------|---------|---------|---------|---------|--------|
| 2015-01-02 | 8395.45 | 8410.60 | 8288.70 | 8288.70 | 101900 |
| 2015-01-05 | 8378.40 | 8445.60 | 8363.90 | 8407.95 | 118200 |
| 2015-01-06 | 8127.35 | 8327.85 | 8111.35 | 8325.29 | 172800 |

---

## 🧑‍💻 Models Used
- **ARIMA** (AutoRegressive Integrated Moving Average)  
- **LSTM** (Long Short-Term Memory neural network)

---

## 📈 Results

### 🔹 ARIMA Forecast
![ARIMA Results](https://github.com/m2kush/market-risk-forecasting/blob/main/results/Screenshot%20from%202025-08-28%2009-29-31.png)



### 🔹 Combined Comparison
![Forecast Comparison](results/forecast_plot.png)

---

## ⚙️ Installation

Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/time-series-forecasting.git
cd time-series-forecasting

## 🙋 Author
KUSH MISHRA  
Connect on GitHub: [m2kush](www.github.com/m2kush)

