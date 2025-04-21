import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.predictor import Predictor, Preprocessor
from components.loan_form import render_form

# Setup Streamlit
st.set_page_config(page_title="Loan Approval Predictor", layout="centered")
st.title("💳 Loan Approval Prediction")
st.caption("A Machine Learning model to predict whether a loan will be approved or not.")

# Load model + preprocessor
@st.cache_resource
def load_predictor():
    preprocessor = Preprocessor(
        encoders_path="models/encoders.pkl",
        scaler_path="models/scaler.pkl",
        imputer_path="models/imputer.pkl"
    )
    predictor = Predictor(
        model_path="models/best_model.pkl",
        preprocessor=preprocessor
    )
    return predictor

predictor = load_predictor()

# Sidebar - Test Case
with st.sidebar:
    st.header("🧪 Test Case Cepat")
    if st.button("🟢 Contoh Disetujui"):
        st.session_state.update({
            'person_age': 35,
            'person_gender': 'male',
            'person_education': 'Bachelor',
            'person_income': 85000,
            'person_emp_exp': 8,
            'person_home_ownership': 'OWN',
            'loan_amnt': 12000,
            'loan_intent': 'DEBTCONSOLIDATION',
            'loan_int_rate': 11.2,
            'loan_percent_income': 0.18,
            'cb_person_cred_hist_length': 6,
            'credit_score': 720,
            'previous_loan_defaults_on_file': 'No'
        })
    if st.button("🔴 Contoh Ditolak"):
        st.session_state.update({
            'person_age': 21,
            'person_gender': 'female',
            'person_education': 'High School',
            'person_income': 14000,
            'person_emp_exp': 1,
            'person_home_ownership': 'RENT',
            'loan_amnt': 18000,
            'loan_intent': 'PERSONAL',
            'loan_int_rate': 19.5,
            'loan_percent_income': 0.9,
            'cb_person_cred_hist_length': 2,
            'credit_score': 520,
            'previous_loan_defaults_on_file': 'Yes'
        })

# Render Form & Predict
user_input = render_form()

if user_input:
    with st.spinner("⏳ Sedang memproses..."):
        result = predictor.predict(user_input)

    if result == 1:
        st.success("✅ Pinjaman kemungkinan **Disetujui**.")
    else:
        st.error("❌ Pinjaman kemungkinan **Ditolak**.")
