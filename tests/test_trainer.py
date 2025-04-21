import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.trainer import Trainer

if __name__ == "__main__":
    trainer = Trainer(csv_path='data/Dataset_A_loan.csv')
    trainer.run_pipeline()
    print("Training process finished")
    print("Model training and saving completed successfully")