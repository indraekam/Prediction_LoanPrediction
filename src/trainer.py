import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
import pickle
import os

class Trainer:
    def __init__(self, csv_path: str, model_dir: str = 'models'):
        self.csv_path = csv_path
        self.model_dir = model_dir
        self.df = None
        self.model = None
        self.label_encoders = {}
        self.imputer = SimpleImputer(strategy='median')
        self.scaler = StandardScaler()

        # Pastikan direktori model tersedia
        os.makedirs(self.model_dir, exist_ok=True)

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        print(f"✅ Data loaded from {self.csv_path}")

    def preprocess_data(self):
        df = self.df.copy()

        # Imputasi person_income
        df['person_income'] = self.imputer.fit_transform(df[['person_income']])

        # Encoding fitur kategorikal
        for col in df.select_dtypes(include='object').columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.label_encoders[col] = le

        # Pisahkan fitur & label
        X = df.drop(columns='loan_status')
        y = df['loan_status']

        # Scaling fitur numerik
        X_scaled = self.scaler.fit_transform(X)

        # Simpan komponen preprocessing
        with open(os.path.join(self.model_dir, 'scaler.pkl'), 'wb') as f:
            pickle.dump(self.scaler, f)

        with open(os.path.join(self.model_dir, 'imputer.pkl'), 'wb') as f:
            pickle.dump(self.imputer, f)

        with open(os.path.join(self.model_dir, 'encoders.pkl'), 'wb') as f:
            pickle.dump(self.label_encoders, f)

        print("✅ Preprocessing selesai dan disimpan")
        return train_test_split(X_scaled, y, test_size=0.2, stratify=y, random_state=42)

    def train_model(self, X_train, y_train):
        self.model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
        self.model.fit(X_train, y_train)
        print("✅ Model trained successfully")

    def save_model(self, filename='best_model.pkl'):
        path = os.path.join(self.model_dir, filename)
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"✅ Model saved to {path}")
    
    def run_pipeline(self):
        self.load_data()
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.train_model(X_train, y_train)
        self.save_model()
        print("✅ Pipeline completed successfully")
