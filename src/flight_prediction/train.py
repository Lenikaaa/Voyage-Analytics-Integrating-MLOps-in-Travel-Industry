import joblib
from pathlib import Path

import pandas as pd
import mlflow
import mlflow.sklearn
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# =========================
# Project paths
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "flight_prediction" / "processed_flights.csv"
MODEL_DIR = BASE_DIR / "model" / "flight_prediction"

# Create model directory if it doesn't exist
MODEL_DIR.mkdir(parents=True, exist_ok=True)

print(f"Reading data from: {DATA_PATH}")
print(f"Saving models to: {MODEL_DIR}")

# =========================
# Load data
# =========================
df = pd.read_csv(DATA_PATH)

X = df.drop("price", axis=1)
y = df["price"]

# Save feature names
joblib.dump(
    X.columns.tolist(),
    MODEL_DIR / "feature_columns.pkl"
)

# =========================
# Train/Test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MLflow tracking
# =========================
with mlflow.start_run():

    params = {
        "n_estimators": 500,
        "learning_rate": 0.08,
        "max_depth": 5,
        "subsample": 0.88,
    }

    mlflow.log_params(params)

    # Train model
    model = XGBRegressor(
        n_estimators=500,
        learning_rate=0.08,
        max_depth=5,
        subsample=0.88,
        random_state=42,
    )

    model.fit(X_train, y_train)

    # Save model
    joblib.dump(
        model,
        MODEL_DIR / "xgb_regressor.pkl"
    )

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log model in MLflow
    # mlflow.sklearn.log_model(
    #    model,
    #    artifact_path="xgb_model"
    # )

print(f"MSE: {mse}")
print(f"R2 Score: {r2}")
print("Training completed successfully.")
print(f"Model saved at: {MODEL_DIR}")