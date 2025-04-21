
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.predictor import Predictor, Preprocessor

preprocessor = Preprocessor(
    encoders_path='models/encoders.pkl',
    scaler_path='models/scaler.pkl',
    imputer_path='models/imputer.pkl'
)

predictor = Predictor(
    model_path='models/best_model.pkl',
    preprocessor=preprocessor
)

sample_input = {
    "person_age": 30,
    "person_gender": "male",
    "person_education": "Bachelor",
    "person_income": 45000,
    "person_emp_exp": 5,
    "person_home_ownership": "RENT",
    "loan_amnt": 15000,
    "loan_intent": "PERSONAL",
    "loan_int_rate": 13.5,
    "loan_percent_income": 0.33,
    "cb_person_cred_hist_length": 4,
    "credit_score": 640,
    "previous_loan_defaults_on_file": "No"
}

result = predictor.predict(sample_input)
print("Hasil prediksi:", "✅ Disetujui" if result == 1 else "❌ Ditolak")
