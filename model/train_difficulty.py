import pandas as pd
import joblib
import json
import time

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    classification_report,
    f1_score,
    accuracy_score,
    precision_score,
    recall_score
)

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC


# =========================
# 1. LOAD & CLEAN DATA
# =========================

df = pd.read_csv("data/difficulty_data.csv")

df["difficulty"] = df["difficulty"].str.strip().str.lower()
df = df[df["difficulty"].isin(["easy", "medium", "hard"])]

X = df["text"]
y = df["difficulty"]

print("Class distribution:")
print(y.value_counts())
print("-" * 40)


# =========================
# 2. SPLIT (70 / 15 / 15)
# =========================

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
)


# =========================
# 3. MODELS
# =========================

models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ),
    "Linear SVM": LinearSVC(
        class_weight="balanced"
    )
}

results = {}
metrics = {}          # 🔥 тут зберігаємо метрики
best_model = None
best_score = 0.0


# =========================
# 4. TRAIN & EVALUATE
# =========================

for name, clf in models.items():
    print(f"\n=== {name} ===")

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            ngram_range=(1, 2),
            min_df=2,
            stop_words="english"
        )),
        ("clf", clf)
    ])

    start_time = time.time()
    pipeline.fit(X_train, y_train)
    train_time = time.time() - start_time

    y_pred = pipeline.predict(X_test)

    # --- metrics ---
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro", zero_division=0)
    rec = recall_score(y_test, y_pred, average="macro", zero_division=0)
    f1 = f1_score(y_test, y_pred, average="macro")

    metrics[name] = {
        "accuracy": round(acc, 3),
        "precision": round(prec, 3),
        "recall": round(rec, 3),
        "f1": round(f1, 3),
        "train_time_ms": int(train_time * 1000)
    }

    results[name] = f1

    print(classification_report(y_test, y_pred))
    print(f"Macro F1-score: {f1:.3f}")

    if f1 > best_score:
        best_score = f1
        best_model = pipeline


# =========================
# 5. RESULTS SUMMARY
# =========================

print("\n=== MODEL COMPARISON ===")
for name, score in results.items():
    print(f"{name}: {score:.3f}")

print("\nBest model:", max(results, key=results.get))
print("Best macro F1:", best_score)


# =========================
# 6. SAVE BEST MODEL
# =========================

joblib.dump(best_model, "model/best_difficulty_model.pkl")
print("\n✅ Best model saved to model/best_difficulty_model.pkl")


# =========================
# 7. SAVE METRICS 
# =========================

with open("model/metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2, ensure_ascii=False)

print("📊 Metrics saved to model/metrics.json")
