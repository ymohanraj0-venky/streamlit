import streamlit as st
from datetime import date, timedelta

st.title("🧑 Bio Data Form")

# Today's date
today = date.today()
# Minimum age = 10 years
max_date = today - timedelta(days=365 * 10)

# Biodata fields
name = st.text_input("Full Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
email = st.text_input("Email")
phone = st.text_input("Phone Number")

# Date of Birth (Calendar with restriction)
dob = st.date_input(
    "Date of Birth (Must be 10+ years old)",
    max_value=max_date
)

# Submit Button
if st.button("Submit"):
    if name and email and phone:
        age = (today - dob).days // 365
        st.success(f"✅ Bio Data Submitted!\n\n"
                   f"**Name:** {name}\n"
                   f"**Gender:** {gender}\n"
                   f"**Email:** {email}\n"
                   f"**Phone:** {phone}\n"
                   f"**Date of Birth:** {dob}\n"
                   f"**Age:** {age} years")
    else:
        st.error("⚠️ Please fill in all details before submitting.")
