import streamlit as st
import pandas as pd
import joblib

# Title
st.title("Dairy Sales Prediction System")

# Load model safely
try:
    model = joblib.load("model.pkl")
    st.success("Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ---------------- INPUTS ---------------- #

price = st.slider("Price per Unit", 20, 120)
units = st.slider("Units Sold", 10, 200)
discount = st.slider("Discount", 0.0, 0.3)
temperature = st.slider("Temperature", 10, 40)
marketing = st.slider("Marketing Spend", 1000, 10000)
competitor_price = st.slider("Competitor Price", 15, 110)

holiday = st.selectbox("Holiday", [0, 1])
weekend = st.selectbox("Weekend", [0, 1])

product = st.selectbox("Product", ["Milk", "Paneer", "Curd", "Butter"])
store = st.selectbox("Store Type", ["Urban", "Rural"])
size = st.selectbox("Store Size", ["Small", "Medium", "Large"])

# Default values (important)
month = 1
day = 1
stock = 200
day_of_week = 3

# ---------------- DATA PREPARATION ---------------- #

data = {
    "Price_per_Unit": price,
    "Units_Sold": units,
    "Holiday": holiday,
    "Temperature": temperature,
    "Discount": discount,
    "Marketing_Spend": marketing,
    "Competitor_Price": competitor_price,
    "Day_of_Week": day_of_week,
    "Is_Weekend": weekend,
    "Stock_Available": stock,
    "Month": month,
    "Day": day,

    # Encoded columns (IMPORTANT)
    "Product_Curd": 1 if product == "Curd" else 0,
    "Product_Milk": 1 if product == "Milk" else 0,
    "Product_Paneer": 1 if product == "Paneer" else 0,

    "Store_Type_Urban": 1 if store == "Urban" else 0,

    "Store_Size_Medium": 1 if size == "Medium" else 0,
    "Store_Size_Small": 1 if size == "Small" else 0
}

# Convert to DataFrame
input_df = pd.DataFrame([data])

# ---------------- PREDICTION ---------------- #

if st.button("Predict Sales"):
    try:
        prediction = model.predict(input_df)
        st.success(f"Predicted Sales: ₹ {round(prediction[0], 2)}")
    except Exception as e:
        st.error(f"Prediction error: {e}")