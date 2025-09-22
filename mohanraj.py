import streamlit as st
from datetime import date

st.title("🧑 Bio Data Form")

# --- Input Fields ---
name = st.text_input("Full Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
email = st.text_input("Email")
phone = st.text_input("Phone Number")

# --- Date of Birth with Calendar ---
dob = st.date_input("Date of Birth (Select from Calendar)")

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
