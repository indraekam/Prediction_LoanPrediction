# src/predictor.py

import pickle
import numpy as np
import pandas as pd

class Preprocessor:
    def __init__(self, encoders_path, scaler_path, imputer_path):
        # Load preprocessing tools
        with open(encoders_path, 'rb') as f:
            self.encoders = pickle.load(f)
        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)
        with open(imputer_path, 'rb') as f:
            self.imputer = pickle.load(f)

    def preprocess(self, raw_input: dict) -> np.ndarray:
        """
        raw_input: dictionary of user input (before encoding/scaling)
        """
        df = pd.DataFrame([raw_input])

        # Imputasi person_income jika kosong
        df['person_income'] = self.imputer.transform(df[['person_income']])

        # Encoding kategorikal
        for col, encoder in self.encoders.items():
            if col in df.columns:
                df[col] = encoder.transform(df[col])
            else:
                raise ValueError(f"Kolom '{col}' tidak ditemukan dalam input!")

        # Scaling seluruh fitur
        X_scaled = self.scaler.transform(df)
        return X_scaled

class Predictor:
    def __init__(self, model_path, preprocessor: Preprocessor):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        self.preprocessor = preprocessor

    def predict(self, raw_input: dict):
        """
        raw_input: dictionary input dari form user (belum diubah)
        """
        X = self.preprocessor.preprocess(raw_input)
        prediction = self.model.predict(X)
        return prediction[0]
