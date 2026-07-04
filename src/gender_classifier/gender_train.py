import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from scipy.sparse import hstack
import joblib

# ==========================
# Project Paths
# ==========================
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "gender_classifier"
MODEL_DIR = BASE_DIR / "model" / "gender_classifier"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

print(f"Reading data from: {DATA_PATH}")
print(f"Saving model to: {MODEL_DIR}")

# ==========================
# Load data
# ==========================
df = pd.read_csv(DATA_PATH / "users.csv")

# Drop unnecessary columns
df = df.drop(columns=["code", "company"])

# Clean target column
df["gender"] = (
    df["gender"]
    .astype(str)
    .str.lower()
    .str.strip()
)

# Encode target
df["gender"] = df["gender"].map({
    "male": 0,
    "female": 1,
    "none": 2
})

# TF-IDF on names
tfidf = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 4),
    min_df=1
)

X_name = tfidf.fit_transform(df["name"])
X_age = df[["age"]].values

X = hstack([X_name, X_age])
y = df["gender"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save artifacts
joblib.dump(model, MODEL_DIR / "model.joblib")
joblib.dump(tfidf, MODEL_DIR / "tfidf.joblib")

# Save processed data
df.to_csv(
    MODEL_DIR / "processed_users.csv",
    index=False
)

print("Gender classifier trained successfully.")
print(f"Model saved at: {MODEL_DIR}")