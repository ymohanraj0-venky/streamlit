import streamlit as st
import datetime
from datetime import date

st.title("🧑 Bio Data Form")

# --- Input Fields ---
name = st.text_input("Full Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
email = st.text_input("Email")
phone = st.text_input("Phone Number")
Age = st.text_input("Age")

# --- Date of Birth with Calendar ---
dop=st.date_input("Pick a date",
              min_value=datetime.date(1900, 1, 1),
              max_value=datetime.date(2100, 12, 31))

# --- Submit Button ---
if st.button("Submit"):
    if name and email and phone:
        today = date.today()
        age = (today - dob).days // 365
        st.success("✅ Bio Data Submitted Successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Date of Birth:** {dob}")
        st.write(f"**Age:** {age} years")
    else:
        st.error("⚠️ Please fill all the required details.")
