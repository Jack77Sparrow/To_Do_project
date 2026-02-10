
import joblib

model = joblib.load("app/model/task_classifier.pkl")
difficulty_model = joblib.load("app/model/best_difficulty_model.pkl")