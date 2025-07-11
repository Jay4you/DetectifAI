import streamlit as st
import pandas as pd
import joblib
import os

# Load model
model_path = "model/scam_model.pkl"
if not os.path.exists(model_path):
    st.error("Model file not found. Please run train_model.py first.")
    st.stop()

model = joblib.load(model_path)

# Page setup
st.set_page_config(page_title="DetectifAI", layout="centered")
st.title("🕵️ DetectifAI")
st.markdown("Detect **phishing**, **smishing**, or **safe** messages using AI trained on Nigerian-style scams.")

# User input
message = st.text_area("📨 Paste an SMS or Email message here:", height=150)

if st.button("🔍 Analyze"):
    if message.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        prediction = model.predict([message])[0]
        if prediction == "phishing":
            st.error("🚨 This message appears to be a **phishing attempt**.")
        elif prediction == "smishing":
            st.warning("⚠️ This message looks like a **smishing (SMS scam)**.")
        else:
            st.success("✅ This message seems **safe**.")

# Optional footer
st.markdown("---")
st.caption("Built with Love by DetectifAI — Securing Nigerian cyberspace.")
