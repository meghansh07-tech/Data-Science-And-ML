import streamlit as st
import joblib
import numpy as np
lm=joblib.load('Linear regression_model.pkl')
st.title("🛍️ Ecommerce Customer Spending Predictor")

st.markdown("""
Predict a customer's **Yearly Amount Spent** based on:

- Average Session Length
- Time on App
- Time on Website
- Length of Membership
""")
col1, col2 = st.columns(2)

with col1:
    avg_session = st.number_input("Avg Session Length", value=33.0)

    time_app = st.number_input("Time on App", value=12.0)

with col2:
    time_website = st.number_input("Time on Website", value=37.0)

    membership = st.number_input("Length of Membership", value=4.0)

st.write("Welcome to my prediction app on  a massive dataset of Ecommerce Customers  Dataset")
feature1 = st.number_input("Avg. Session Length", value=0)
feature2 = st.number_input("Time on the App", value=0)
feature3 =st.number_input("Time on the Website", value=0)
feature4 = st.number_input("Length of Membership", value=0)
st.sidebar.header("Model Information")

st.sidebar.write("""
Algorithm: Linear Regression

Dataset: Ecommerce Customers

Features: 4

Target: Yearly Amount Spent
""")

if st.button("🚀 Predict Spending"):
    prediction =lm.predict(np.array([[feature1,feature2,feature3,feature4]]))
    st.success(
        f"💰 Predicted Yearly Spending: ${prediction[0]:,.2f}"
    )