# 💳 Loan Approval Prediction App

> A Machine Learning project to predict whether a loan application is likely to be **approved** or **rejected**, built with XGBoost and deployed using Streamlit.

---

![banner](assets/banner.png)

---

## 📌 Project Overview

This project:
- Classifies loan approval status based on user financial input
- Compares Random Forest and XGBoost (XGBoost chosen as best model)
- Implements end-to-end training using OOP structure
- Includes preprocessing pipeline (LabelEncoder, Imputer, Scaler)
- Built and deployed with Streamlit

---

## 📂 Folder Structure

```
loan-approval-predictor/
├── app/                # Streamlit frontend
├── components/         # Form UI for prediction
├── models/             # Saved model and preprocessing files
├── src/                # OOP training and inference
├── tests/              # Unit test files
├── notebook/           # EDA and experimentation
└── README.md
```

---

## 📊 Exploratory Data Analysis & Modeling

The full EDA, model development, evaluation, and saving process is documented in the notebook:

📁 `notebook/Loan_Prediction.ipynb`

### Key steps covered in the notebook:
- Data loading and inspection
- Handling missing values (e.g. `person_income`)
- Label encoding for categorical features
- Scaling of numerical features
- Model training (Random Forest & XGBoost)
- Evaluation using classification metrics and confusion matrix
- Exporting the best model and preprocessing pipeline to `.pkl` files

This notebook served as the basis for the OOP-refactored training module in `src/trainer.py` and the deployment-ready app in `app/app.py`.

---

## 🚀 Streamlit App Features

- 👤 Input form for user loan data
- 🔍 Real-time prediction: Approved / Rejected
- 🧪 Sidebar Test Case (Approved & Rejected)
- 🧼 Auto preprocessing: encoding, imputing, scaling

---

## 🔧 How to Run Locally

```bash
# Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app/app.py
```

---

## 🧠 Model & Tech Stack

- `XGBoostClassifier`
- `scikit-learn`
- `Streamlit`
- `OOP Python`
- `pickle` for model persistence

---

## 🎓 Author

Built with 💙 by **Indra Eka Mandriana, S.Kom**  
Machine Learning Engineer | Tutor Informatika

---

## 📸 Screenshot

![screenshot](assets/screenshot.png)

---

## 🌍 Live Demo

🚀 *Coming soon on Streamlit Cloud or Hugging Face Spaces*