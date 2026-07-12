import streamlit as st
import joblib
import numpy as np
import mysql.connector

# Load your predictive machine learning model file
lm = joblib.load('Linear regression_model.pkl')

st.title("🛍️ Ecommerce Customer Spending Predictor")

st.markdown("""
Predict a customer's **Yearly Amount Spent** based on:

- Average Session Length
- Time on App
- Time on Website
- Length of Membership
""")

# Side Bar Metadata Info
st.sidebar.header("Model Information")
st.sidebar.write("""
Algorithm: Linear Regression
Dataset: Ecommerce Customers
Features: 4
Target: Yearly Amount Spent
""")

st.write("Welcome to my prediction app on a massive dataset of Ecommerce Customers Dataset")

# 1. Create a SINGLE set of layout columns and variables
col1, col2 = st.columns(2)

with col1:
    avg_session = st.number_input("Avg. Session Length", value=33.0)
    time_app = st.number_input("Time on App", value=12.0)

with col2:
    time_website = st.number_input("Time on Website", value=37.0)
    membership = st.number_input("Length of Membership", value=4.0)

# Trigger button processing
if st.button("🚀 Predict Spending"):
    # 2. Generate model outputs using our actual variables
    prediction = lm.predict(np.array([[avg_session, time_app, time_website, membership]]))
    predicted_value = float(prediction[0])

    # Render successful output prediction to the web interface
    st.success(f"💰 Predicted Yearly Spending: ${predicted_value:,.2f}")

    # 3. Open automated data pipeline connection to local MySQL server
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MEGHANSH@123",  # 🧠 Put your real password here
            database="ml_app"
        )
        cursor = conn.cursor()

        # SQL table structure layout matching your new schema
        query = """
            INSERT INTO prediction_logs 
            (avg_session_length, time_on_app, time_on_website, length_of_membership, predicted_spending)
            VALUES (%s, %s, %s, %s, %s)
        """

        # 4. CRITICAL: Pass the exact same variables we used for prediction
        record_tuple = (avg_session, time_app, time_website, membership, predicted_value)

        cursor.execute(query, record_tuple)
        conn.commit()  # Flush operational data to physical database disk tables

        st.info("📊 This prediction and its metrics have been logged securely into MySQL!")

    except Exception as e:
        st.error(f"⚠️ Could not log data to MySQL: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()