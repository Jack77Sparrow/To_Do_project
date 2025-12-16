import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/training_data.csv")

X = df["text"]
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = Pipeline([
    ("tfidf", TfidfVectorizer(
    ngram_range=(1, 3),
    max_features=8000,
    stop_words="english"
)),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "model/task_classifier.pkl")
