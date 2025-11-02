import streamlit as st
import requests

st.set_page_config(page_title="🌍 Real Time Currency Exchange", layout="centered")

st.title("💱 Real Time Currency Exchange")

# --- Currency selection ---
currencies = ["PKR", "USD", "SAR", "AED", "GBP", "EUR", "CNY", "CAD", "AUD", "INR"]

col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox("From Currency:", currencies, index=0)
with col2:
    to_currency = st.selectbox("To Currency:", currencies, index=1)

amount = st.number_input("Enter Amount:", min_value=1.0, step=1.0)

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            converted_amount = amount * rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error("Selected target currency not available.")
    else:
        st.error("⚠️ Failed to fetch exchange rates. Try again later.")
