import streamlit as st

def render_form():
    with st.form("loan_form"):
        st.subheader("📝 Form Input Calon Peminjam")

        col1, col2 = st.columns(2)

        with col1:
            person_age = st.number_input("Usia", 18, 100, value=st.session_state.get('person_age', 30))
            person_gender = st.selectbox("Jenis Kelamin", ["male", "female"], index=["male", "female"].index(st.session_state.get('person_gender', 'male')))
            person_education = st.selectbox("Pendidikan", ["High School", "Bachelor", "Master"], index=["High School", "Bachelor", "Master"].index(st.session_state.get('person_education', 'Bachelor')))
            person_income = st.number_input("Pendapatan Tahunan", 0, 200000, value=st.session_state.get('person_income', 40000))
            person_emp_exp = st.number_input("Pengalaman Kerja (Tahun)", 0, 50, value=st.session_state.get('person_emp_exp', 5))
            person_home_ownership = st.selectbox("Status Tempat Tinggal", ["RENT", "OWN", "MORTGAGE", "OTHER"], index=["RENT", "OWN", "MORTGAGE", "OTHER"].index(st.session_state.get('person_home_ownership', 'RENT')))

        with col2:
            loan_amnt = st.number_input("Jumlah Pinjaman", 500, 50000, value=st.session_state.get('loan_amnt', 10000))
            loan_intent = st.selectbox("Tujuan Pinjaman", ["PERSONAL", "MEDICAL", "EDUCATION", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"], index=["PERSONAL", "MEDICAL", "EDUCATION", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"].index(st.session_state.get('loan_intent', 'PERSONAL')))
            loan_int_rate = st.number_input("Suku Bunga (%)", 5.0, 30.0, value=st.session_state.get('loan_int_rate', 13.0))
            loan_percent_income = st.number_input("Rasio Pinjaman vs Pendapatan", 0.0, 1.0, value=st.session_state.get('loan_percent_income', 0.3))
            cb_person_cred_hist_length = st.number_input("Lama Riwayat Kredit (Tahun)", 0, 20, value=st.session_state.get('cb_person_cred_hist_length', 4))
            credit_score = st.number_input("Skor Kredit", 300, 850, value=st.session_state.get('credit_score', 650))
            previous_loan_defaults_on_file = st.selectbox("Pernah Gagal Bayar?", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.get('previous_loan_defaults_on_file', 'No')))

        submitted = st.form_submit_button("🔍 Prediksi Sekarang")

        if submitted:
            return {
                "person_age": person_age,
                "person_gender": person_gender,
                "person_education": person_education,
                "person_income": person_income,
                "person_emp_exp": person_emp_exp,
                "person_home_ownership": person_home_ownership,
                "loan_amnt": loan_amnt,
                "loan_intent": loan_intent,
                "loan_int_rate": loan_int_rate,
                "loan_percent_income": loan_percent_income,
                "cb_person_cred_hist_length": cb_person_cred_hist_length,
                "credit_score": credit_score,
                "previous_loan_defaults_on_file": previous_loan_defaults_on_file
            }

    return None
