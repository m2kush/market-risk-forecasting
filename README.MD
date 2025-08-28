# 📈 Time Series Forecasting with ARIMA and LSTM

## 🔍 Overview
This project explores **time series forecasting** using two approaches:
- **ARIMA** (AutoRegressive Integrated Moving Average) – a classical statistical method.  
- **LSTM** (Long Short-Term Memory) – a deep learning approach with PyTorch.  

The dataset used is stock market index data (`^NSEI`), but the framework can be applied to any univariate time series.

---

## 🚀 Features
- Preprocessing and train-test split  
- ARIMA model training and forecasting  
- LSTM model built in PyTorch  
- Visualization of **Actual vs Predicted** values  
- Comparison of statistical vs deep learning methods  

---

## 🛠 Installation
Clone this repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/time-series-forecasting.git
cd time-series-forecasting
pip install -r requirements.txt
```


## Project structure 
time-series-forecasting/
│── data/                # (optional) dataset or sample CSV
│── notebooks/           # Jupyter notebooks
│── src/                 # Python scripts (models, training, utils)
│── results/             # Plots, metrics
│── requirements.txt     # Dependencies
│── README.md            # Documentation


## 📊 Usage
```bash
jupyter notebook notebooks/forecasting.ipynb
```

Run the Jupyter notebook for training and evaluation:


## 📈 Results

Example visualization of predictions vs actual values:

## 🔮 Future Work

Hyperparameter tuning for ARIMA and LSTM

Add models like Prophet / Transformers

Deploy as a web app for real-time predictions

