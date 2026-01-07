# Sample-Code demonstrating how an ML model gets deployed using streamlit.

import streamlit as st
import joblib

model = joblib.load("rf_volatility_model.pkl")

st.title("Crypto Volatility Predictor") # Displays the title
st.write("Predict next-day Bitcoin Volatility") # A short description

# Create User Input Fields
vol_lag1 = st.number_input("Volatility Lag 1")
vol_lag3 = st.number_input("Volatility Lag 3")
vol_lag7 = st.number_input("Volatility Lag 7")
vol_lag14 = st.number_input("Volatility Lag 14")
abs_ret = st.number_input("Absolute Return")
liq = st.number_input("Liquidity Ratio")
h1 = st.number_input("High-Low Range")

# Creates a button labeled Predict
if st.button("Predict"):
    pred = model.predict([[vol_lag1, vol_lag3, vol_lag7, vol_lag14, abs_ret, liq, h1]])
    st.success(f"Predicted Volatility: {pred[0]: .4f}")