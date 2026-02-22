# Cryptocurrency Volatility Prediction (Bitcoin)

## Overview
This project majorly focuses on predicting next-day cryptocurrency volatility using historical Bitcoin market data.  
Volatility is computed using rolling standard deviation of daily log returns, and a machine learning model is trained to forecast future market risk.

The objective is to build a robust regression model capable of predicting next-day volatility using engineered financial features.

---

##  Problem Statement
Cryptocurrency markets are highly volatile and unpredictable.  
Understanding and forecasting volatility helps investors and analysts assess market risk.

This project aims to:
- Compute rolling volatility using historical price data
- Engineer meaningful financial features
- Predict next-day volatility using machine learning
- Compare performance with a naive baseline model

---

## Dataset
- Historical cryptocurrency price data
- Features include: Open, High, Low, Close, Volume, MarketCap
- 72,946 total rows (multiple cryptocurrencies)
- Filtered to Bitcoin: 3,012 clean records after preprocessing
- Time range: 2013 – 2022

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

##  Project Workflow

### 1. Data Loading & Cleaning
- Extracted dataset from zip file
- Removed unnecessary columns
- Converted date column to datetime
- Sorted chronologically (required for time-series modeling)
- Removed zero-volume rows

### 2. Volatility Calculation (Core Step)
- Computed daily log returns  
- Calculated 7-day rolling standard deviation as volatility  
- Created next-day volatility as target variable

### 3. Feature Engineering
Created financial features including:
- Absolute returns
- High-Low spread
- Liquidity ratio (Volume / MarketCap)
- Lagged volatility features (1, 3, 7, 14 days)

### 4. Exploratory Data Analysis (EDA)
- Price trend visualization
- Volatility trend analysis
- Correlation heatmap of numerical features

### 5. Time-Based Train-Test Split
- 80% Training Data
- 20% Testing Data
- No data leakage (chronological split)

---

##  Model Used
### Random Forest Regressor

Chosen because:
- Handles non-linear relationships
- Robust to noise
- Requires minimal feature scaling
- Strong baseline for financial regression problems

---

##  Model's Performance

### Base Model:
- Train RMSE: 0.00992
- Test RMSE: 0.00945
- Test MAE: 0.00663
- Test R²: 0.697

### Naive Baseline RMSE:
- 0.01137

- The model outperformed the naive baseline  
- No overfitting observed (Test RMSE slightly lower than Train RMSE)  
- Model captures meaningful volatility patterns

---

##  Model Optimization
Hyperparameter tuning performed with deeper forest:
- Tuned Test RMSE: 0.00936
- Performance improvement observed

---

##  Visualizations
- Actual vs Predicted Volatility
- Feature Importance Plot
- Price & Volatility Trends
- Correlation Heatmap

---

##  Project Structure
data/ → Raw dataset
src/ → Source code
Report section/ → Project documentation

---

##  Future Improvements
- Implement LSTM / Deep Learning models
- Add technical indicators (RSI, MACD, Bollinger Bands)
- Multi-crypto modeling instead of single-asset
- Real-time volatility prediction

---

##  Key Learnings
- Financial time-series modeling
- Volatility computation using log returns
- Feature engineering for market prediction
- Avoiding data leakage in time-based splits
- Model evaluation & baseline comparison
